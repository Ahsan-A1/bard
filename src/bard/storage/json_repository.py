import json
import os
from collections.abc import Callable
from pathlib import Path
from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class JsonRepository(Generic[T]):
    def __init__(
        self,
        path: Path,
        model: type[T],
        pk_getter: Callable[[T], str] = lambda e: e.id,  # type: ignore[attr-defined]
    ) -> None:
        self._path = path
        self._model = model
        self._pk = pk_getter
        self._data: dict[str, T] = {}

    def load(self) -> None:
        if not self._path.exists():
            self._data = {}
            return
        raw = json.loads(self._path.read_text(encoding="utf-8"))
        entities = [self._model.model_validate(item) for item in raw]
        self._data = {self._pk(e): e for e in entities}

    def get(self, pk: str) -> T | None:
        return self._data.get(pk)

    def all(self) -> list[T]:
        return list(self._data.values())

    def save(self, entity: T) -> None:
        self._data[self._pk(entity)] = entity
        self._flush()

    def delete(self, pk: str) -> None:
        self._data.pop(pk, None)
        self._flush()

    def _flush(self) -> None:
        self._path.parent.mkdir(parents=True, exist_ok=True)
        serialized = [m.model_dump(mode="json") for m in self._data.values()]
        tmp = self._path.with_suffix(self._path.suffix + ".tmp")
        tmp.write_text(json.dumps(serialized, indent=2), encoding="utf-8")
        os.replace(tmp, self._path)
