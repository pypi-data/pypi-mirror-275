from collections.abc import Callable
from typing import Literal, Optional, TypedDict

from langchain.prompts.prompt import PromptTemplate
from langsmith.evaluation import LangChainStringEvaluator
from langsmith.schemas import Example, Run

from langsmith_evaluation_helper.llm.model import ChatModel



class BuiltinEvaluatorConfig(TypedDict):
    type: Literal["length", "llm-judge", "similar"]
    value: str
    label: Optional[str]  # noqa: UP007


class EvalResult(TypedDict):
    key: str | None
    score: float


Evaluator = Callable[[Run, Example], EvalResult | LangChainStringEvaluator]


def generate_builtin_evaluator_functions(evaluator_configs: list[BuiltinEvaluatorConfig]) -> list[Evaluator]:
    evaluators = []

    for evaluator_config in evaluator_configs:
        if evaluator_config["type"] == "length":

            def create_length_evaluator(evaluator_config: BuiltinEvaluatorConfig) -> Evaluator:
                def length_evaluator(run: Run, example: Example) -> EvalResult:
                    output = None
                    if run.outputs is not None:
                        output = run.outputs.get("output", None)
                    if output is None:
                        return {"key": "length", "score": False}
                    value = evaluator_config["value"]
                    score = False

                    try:
                        if "<=" in value:
                            score = len(output) <= int(value.replace("<=", "").strip())
                        elif "<" in value:
                            score = len(output) < int(value.replace("<", "").strip())
                        elif ">=" in value:
                            score = len(output) >= int(value.replace(">=", "").strip())
                        elif ">" in value:
                            score = len(output) > int(value.replace(">", "").strip())
                        else:
                            raise ValueError
                    except Exception:
                        print(f"[Warning] Invalid integer value in evaluator_config['value']: {value}")
                        return {"key": "length", "score": False}

                    return {"key": "length", "score": score}

                return length_evaluator

            evaluators.append(create_length_evaluator(evaluator_config))
        elif evaluator_config["type"] == "llm-judge":

            def create_llm_judge_evaluator(evaluator_config: BuiltinEvaluatorConfig) -> Evaluator:
                def llm_judge_evaluator(run: Run, example: Example) -> EvalResult:
                    model = ChatModel(temperature=0.7, verbose=True)
                    evaluate_prompt = """Evaluate and give a score between 0 to 1 the following text with the evaluation perspective specified in the prompt.

                  evaluation perspective: {evaluation_perspective}
                  text: {text}

                  only output the score
                  """

                    prompt = PromptTemplate.from_template(evaluate_prompt)
                    inputs = {}
                    if run.outputs is not None:
                        inputs = {
                            "evaluation_perspective": evaluator_config["value"],
                            "text": run.outputs.get("output"),
                        }

                    key = evaluator_config.get("label", "llm-judge")
                    score = float(model.invoke(prompt=prompt, **inputs))
                    return {
                        "key": key,
                        "score": score,
                    }

                return llm_judge_evaluator

            evaluators.append(create_llm_judge_evaluator(evaluator_config))
        elif evaluator_config["type"] == "similar":

            def similar_evaluator(run: Run, example: Example) -> LangChainStringEvaluator:
                return LangChainStringEvaluator("embedding_distance")

            evaluators.append(similar_evaluator)
        else:
            print(f"[Warning] Unknown evaluator type: {evaluator_config['type']}")

    return evaluators
