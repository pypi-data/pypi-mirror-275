from enum import Enum
from langchain.chat_models.base import BaseChatModel
from typing import Any
from langchain_openai import AzureChatOpenAI, ChatOpenAI
from langchain_core.pydantic_v1 import SecretStr
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import Runnable, RunnableConfig
from langchain.schema.output_parser import StrOutputParser


class ChatModelName(Enum):
    TURBO = "gpt-3.5-turbo"
    GPT4 = "gpt-4-0613"
    GPT4_32K = "gpt-4-32k-0613"
    AZURE_GPT35_16K_TURBO = "gpt-35-turbo"
    AZURE_GPT4_32K = "gpt-4-32k"
    GEMINI_PRO = "gemini-pro"
    CLAUDE3_SONNET = "claude3-sonnet"


AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY", "")
AZURE_OPENAI_API_BASE = os.getenv("AZURE_OPENAI_API_BASE", "")


def get_chat_model(name: ChatModelName, **kwargs: Any) -> BaseChatModel:
    if name == ChatModelName.TURBO or name == ChatModelName.GPT4 or name == ChatModelName.GPT4_32K:
        return ChatOpenAI(model=name.value, **kwargs)
    elif name == ChatModelName.AZURE_GPT35_16K_TURBO:
        return AzureChatOpenAI(
            api_key=SecretStr(AZURE_OPENAI_API_KEY),
            azure_endpoint=AZURE_OPENAI_API_BASE,
            api_version="2023-08-01-preview",
            azure_deployment="gpt-35-turbo-16k-dev",
            **kwargs,
        )
    elif name == ChatModelName.AZURE_GPT4_32K:
        return AzureChatOpenAI(
            api_key=SecretStr(AZURE_OPENAI_API_KEY),
            azure_endpoint=AZURE_OPENAI_API_BASE,
            api_version="2023-08-01-preview",
            azure_deployment="gpt-4-32k-dev",
            **kwargs,
        )
    elif name == ChatModelName.GEMINI_PRO:
        return ChatGoogleGenerativeAI(
            model="gemini-pro",
            **kwargs,
        )
    elif name == ChatModelName.CLAUDE3_SONNET:
        return ChatAnthropic(model_name="claude-3-sonnet-20240229", **kwargs)
    else:
        raise ValueError(f"Invalid model name. {name}")
    

class ChatModel: 
    """ Facade wrapper class to handle lifecycle of Langchain's basechatmodel."""
    default_model: BaseChatModel
    default_model_name: ChatModelName
    verbose: bool = True
    kwargs: Any

    def __init__(self, default_model_name: ChatModelName = ChatModelName.CLAUDE3_SONNET, **kwargs: Any) -> None:
        self.default_model = get_chat_model(default_model_name, **kwargs)
        self.default_model_name = default_model_name
        self.kwargs = kwargs

    def get_model(self, model_name: ChatModelName | None = None) -> BaseChatModel:
        model = self.default_model
        if model_name:
            model = get_chat_model(model_name, **self.kwargs)

        return model
    
    def invoke(
            self,
            prompt: PromptTemplate,
            tags: list[str] | None = None,
            model_name: ChatModelName | None = None,
            metadata: dict[str, Any] | None = None,
            **kwargs: Any,
    ) -> str:
        chain = (prompt | self.get_model(model_name)) | StrOutputParser()
        config = RunnableConfig(
            tags=tags or [],
            metadata=metadata or {},
        )

        return chain.invoke(input=kwargs, config=config)

    async def async_invoke(
        self,
        prompt: PromptTemplate,
        tags: list[str] | None = None,
        model_name: ChatModelName | None = None,
        metadata: dict[str, Any] | None = None,
        **kwargs: Any,
    ) -> str:
        chain = prompt | self.get_model(model_name) | StrOutputParser()
        config = RunnableConfig(
            tags=tags or [],
            metadata=metadata or {},
        )

        return await chain.ainvoke(input=kwargs, config=config)