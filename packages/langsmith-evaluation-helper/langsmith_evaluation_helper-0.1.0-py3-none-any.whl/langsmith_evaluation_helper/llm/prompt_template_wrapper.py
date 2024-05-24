from typing import Generic, TypeVar

from pydantic import BaseModel

PromptInput = TypeVar("PromptInput", bound=BaseModel)


class InputTypedPromptTemplate(BaseModel, Generic[PromptInput]):
    template: str
    input: PromptInput