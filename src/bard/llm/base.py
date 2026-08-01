from abc import ABC, abstractmethod
from typing import TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class LLMClient(ABC):
    @abstractmethod
    def query(self, prompt: str) -> str: ...

    @abstractmethod
    def query_structured(self, prompt: str, schema: type[T]) -> T: ...
