from datetime import UTC, datetime

from pydantic import BaseModel, Field


class Checkpoint(BaseModel):
    description: str
    achieved: bool = False
    notes: str = ""


class Summary(BaseModel):
    covers_turns: list[str] = Field(default_factory=list)
    text: str


class Story(BaseModel):
    id: str
    title: str = ""
    base_prompt: str
    plan: str = ""
    checkpoints: list[Checkpoint] = Field(default_factory=list)
    turn_ids: list[str] = Field(default_factory=list)
    summaries: list[Summary] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
