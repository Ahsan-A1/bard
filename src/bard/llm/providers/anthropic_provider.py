from typing import TypeVar

from pydantic import BaseModel

from ..base import LLMClient

T = TypeVar("T", bound=BaseModel)


class AnthropicClient(LLMClient):
    def __init__(self, api_key: str, model: str) -> None:
        self._api_key = api_key
        self._model = model

    def query(self, prompt: str) -> str:
        raise NotImplementedError

    def query_structured(self, prompt: str, schema: type[T]) -> T:
        raise NotImplementedError
