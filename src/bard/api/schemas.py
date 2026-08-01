from pydantic import BaseModel


class CreateStoryRequest(BaseModel):
    base_prompt: str


class PlayTurnRequest(BaseModel):
    action: str
    generate_image: bool = False


class StorySummary(BaseModel):
    id: str
    title: str
    created_at: str
