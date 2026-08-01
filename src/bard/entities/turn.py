from datetime import UTC, datetime
from typing import Any

from pydantic import BaseModel, Field


class DialogueLine(BaseModel):
    character_id: str
    text: str


class Turn(BaseModel):
    id: str
    story_id: str
    action: str
    narration: str = ""
    dialogue: list[DialogueLine] = Field(default_factory=list)
    state_deltas: dict[str, Any] = Field(default_factory=dict)
    plan_invalidated: bool = False
    image_ref: str | None = None
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
