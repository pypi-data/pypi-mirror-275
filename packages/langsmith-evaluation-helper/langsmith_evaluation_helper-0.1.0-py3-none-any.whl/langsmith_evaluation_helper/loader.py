import asyncio
import importlib.util
import inspect
import os
import sys
from collections.abc import Awaitable, Callable, Coroutine
from typing import Any

import yaml

from langsmith_evaluation_helper.builtin_evaluators import generate_builtin_evaluator_functions
from langchain.prompts import PromptTemplate
from langsmith import aevaluate, evaluate, traceable

from langsmith_evaluation_helper.llm.model import ChatModel, ChatModelName
from langsmith_evaluation_helper.llm.prompt_template_wrapper import InputTypedPromptTemplate


LANGCHAIN_TENANT_ID = os.getenv("LANGCHAIN_TENANT_ID", None)


def is_async_function(func: Callable[..., Any]) -> bool:
    return inspect.iscoroutinefunction(func) or inspect.isasyncgenfunction(func)


def has_inputs_argument(func: Callable[..., Any]) -> bool:
    signature = inspect.signature(func)
    parameters = signature.parameters
    return "inputs" in parameters


def get_prompt_template_and_kwargs_from_input_typed_prompt_template(
    prompt: InputTypedPromptTemplate,
) -> tuple[PromptTemplate, dict[str, Any]]:
    return PromptTemplate.from_template(prompt.template), prompt.input.model_dump()


def get_prompt_template_and_kwargs_from_inputs(
    prompt: str, inputs: dict[Any, Any]
) -> tuple[PromptTemplate, dict[str, Any]]:
    kwargs: dict[str, Any] = {}
    for key, _ in inputs.items():
        kwargs[key] = inputs.get(key, "Unknown")

    return PromptTemplate.from_template(prompt), kwargs


@traceable
def execute_prompt(inputs: dict[Any, Any], prompt: str | InputTypedPromptTemplate, provider: dict[Any, Any]) -> str:
    if isinstance(prompt, str):
        _prompt_template, kwargs = get_prompt_template_and_kwargs_from_inputs(prompt, inputs)
    elif isinstance(prompt, InputTypedPromptTemplate):
        _prompt_template, kwargs = get_prompt_template_and_kwargs_from_input_typed_prompt_template(prompt)
    else:
        raise ValueError(f"Invalid prompt type: {type(prompt)}")

    messages = _prompt_template.format(**kwargs)
    formatted_messages = PromptTemplate.from_template(messages)

    model_id = provider["id"]
    model = getattr(ChatModelName, model_id, None)

    temperature = provider["config"]["temperature"]
    if model is not None:
        llm = ChatModel(default_model_name=model, temperature=temperature, verbose=True)
    else:
        raise ValueError(f"Invalid model_id: {model_id}")
    result = llm.invoke(formatted_messages)
    return result


def load_config(config_path: Any) -> dict[str, Any]:
    """
    Loads config file as YML dictionary.
    """
    with open(config_path) as file:
        config = yaml.safe_load(file)
    return config


def load_function(module_path: str, function_name: str) -> Any:
    """
    Dynamically load a function from a given module.
    """
    if not isinstance(module_path, str) or not module_path:
        raise ValueError("Invalid or empty module path.")
    if not isinstance(function_name, str) or not function_name:
        raise ValueError("Invalid or empty function name.")

    try:
        spec = importlib.util.spec_from_file_location("module", module_path)
        if spec is None:
            raise ImportError(f"Cannot find module specification for the path: {module_path}")

        module = importlib.util.module_from_spec(spec)
        if spec.loader is None:
            raise ImportError("Module loader is not available.")
        spec.loader.exec_module(module)

        if not hasattr(module, function_name):
            raise AttributeError(f"Function '{function_name}' not found in module '{module_path}'")
    except (ImportError, AttributeError) as error:
        print(f"Error: {error}")
        raise
    return getattr(module, function_name)


def load_prompt(config: dict[Any, Any]) -> Any:
    """
    Load the config file and execute the specified entry function.
    """
    prompt_info = config["prompt"]
    script_path = os.path.join(os.path.dirname(config_path), prompt_info["name"])
    function_name = prompt_info["entry_function"]

    func = load_function(script_path, function_name)

    return func


def load_prompt_function(
    config: dict[Any, Any], prompt_config: dict[Any, Any]
) -> Callable[[dict[str, Any]], Any] | Callable[[dict[str, Any]], Coroutine[Any, Any, Any]]:
    prompt_func = load_prompt(prompt_config)
    is_async = is_async_function(prompt_func)

    if is_async:

        async def arun(inputs: dict[Any, Any]) -> Any:
            return await prompt_func(inputs)

        return arun

    def run(inputs: dict[Any, Any]) -> Any:
        return prompt_func(inputs)

    return run


def load_prompt_template(
    prompt_config: dict[Any, Any], provider: dict[Any, Any]
) -> Callable[[dict[str, Any]], str] | Callable[[dict[str, Any]], Awaitable[str]]:
    prompt_func = load_prompt(prompt_config)
    is_async = is_async_function(prompt_func)
    has_inputs = has_inputs_argument(prompt_func)

    async def run_async(inputs: dict[str, Any]) -> str:
        prompt = await prompt_func(inputs) if has_inputs else await prompt_func()
        return execute_prompt(inputs, prompt, provider)

    def run_sync(inputs: dict[str, Any]) -> str:
        prompt = prompt_func(inputs) if has_inputs else prompt_func()
        return execute_prompt(inputs, prompt, provider)

    return run_async if is_async else run_sync


def load_running_prompt_function(config: dict[Any, Any], provider: dict[Any, Any]) -> Callable[[dict[Any, Any]], Any]:
    prompt_config = config["prompt"]
    is_function = prompt_config.get("is_function", False)

    if is_function:
        return load_prompt_function(config, prompt_config)
    else:
        return load_prompt_template(config, provider)


def load_dataset(config: dict[Any, Any]) -> tuple[Any, Any]:
    test_info = config["tests"]
    type = test_info["type"]

    if type == "langsmith_db":
        dataset_name = test_info["dataset_name"]
        experiment_prefix = test_info["experiment_prefix"]
        return (dataset_name, experiment_prefix)
    else:
        return (None, None)


def load_evaluators(config: dict[Any, Any]) -> tuple[Any, Any]:
    builtin_evaluators_config = config["tests"].get("assert", [])
    builtin_evaluators = generate_builtin_evaluator_functions(builtin_evaluators_config)

    evaluators_file_path = os.path.join(os.path.dirname(config_path), config["evaluators_file_path"])
    evaluators = load_function(evaluators_file_path, "evaluators") + builtin_evaluators
    summary_evaluators = load_function(evaluators_file_path, "summary_evaluators")

    return evaluators, summary_evaluators


async def run_evaluate(provider: dict[Any, Any], experiment_prefix: str, **kwargs: dict[str, Any]) -> tuple[Any, Any]:
    experiment_prefix_provider = experiment_prefix + provider["id"]
    prompt_func = load_running_prompt_function(config_file, provider)

    is_async = is_async_function(prompt_func)

    common_args = {
        "experiment_prefix": experiment_prefix_provider,
        "metadata": {
            "prompt_version": "1",
        },
        **kwargs,
    }

    if is_async:
        result = await aevaluate(prompt_func, **common_args)
        dataset_id = await result._manager.get_dataset_id()
    else:
        result = evaluate(prompt_func, **common_args)
        dataset_id = result._manager.dataset_id
    experiment_id = None
    if result._manager and result._manager._experiment and result._manager._experiment.id is not None:
        experiment_id = result._manager._experiment.id.__str__()

    return dataset_id, experiment_id


async def main(config_file: dict[Any, Any]) -> None:
    dataset_name, experiment_prefix = load_dataset(config_file)
    evaluators, summary_evaluators = load_evaluators(config_file)
    max_concurrency = config_file["tests"].get("max_concurrency", None)
    providers = config_file["providers"]

    dataset_id = None
    experiment_ids = []

    tasks = [
        run_evaluate(
            provider,
            experiment_prefix,
            data=dataset_name,
            evaluators=evaluators,
            summary_evaluators=summary_evaluators,
            max_concurrency=max_concurrency,
        )
        for provider in providers
    ]

    # Run all tasks concurrently using asyncio.gather
    results = await asyncio.gather(*tasks)

    # Unpack results and collect dataset and experiment IDs
    for _dataset_id, experiment_id in results:
        dataset_id = _dataset_id
        experiment_ids.append(experiment_id)

    # Print the final comparison URL if there are multiple providers
    if len(providers) > 1:
        seed_url = "https://smith.langchain.com/o/"
        experiment_id_query_str = "%2C".join(experiment_ids)

        url = (
            f"{seed_url}{LANGCHAIN_TENANT_ID}/datasets/{dataset_id}/compare?selectedSessions={experiment_id_query_str}"
        )
        print(url)


if __name__ == "__main__":
    config_path = sys.argv[1] if len(sys.argv) > 1 else "config.yml"
    config_file = load_config(config_path)

    asyncio.run(main(config_file))
