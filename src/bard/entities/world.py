from typing import Literal

from pydantic import BaseModel, Field


class Event(BaseModel):
    description: str
    status: Literal["pending", "triggered"] = "pending"


class Location(BaseModel):
    name: str
    description: str = ""
    landmarks: list[str] = Field(default_factory=list)
    events: list[Event] = Field(default_factory=list)


class World(BaseModel):
    story_id: str
    locations: list[Location] = Field(default_factory=list)
    events: list[Event] = Field(default_factory=list)
    facts: list[str] = Field(default_factory=list)
