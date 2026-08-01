from pydantic import BaseModel, Field


class Character(BaseModel):
    id: str
    story_id: str
    name: str
    description: str = ""
    voice_id: str = ""
    health: int = 100
    traits: list[str] = Field(default_factory=list)
    inventory: list[str] = Field(default_factory=list)
