from typing import TypeVar

from pydantic import BaseModel

from .base import LLMClient

T = TypeVar("T", bound=BaseModel)


class LLMService:
    def __init__(self, client: LLMClient) -> None:
        self._client = client

    def generate(self, prompt: str) -> str:
        raise NotImplementedError

    def generate_structured(self, prompt: str, schema: type[T]) -> T:
        raise NotImplementedError
