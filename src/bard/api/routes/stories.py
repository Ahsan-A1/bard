from fastapi import APIRouter, HTTPException

from ...controllers import story_controller
from ...entities import Story
from ..schemas import CreateStoryRequest

router = APIRouter(prefix="/stories", tags=["stories"])


@router.post("", response_model=Story, status_code=201)
def create_story(body: CreateStoryRequest) -> Story:
    try:
        return story_controller.create_story(body.base_prompt)
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail="create_story not implemented") from e


@router.get("", response_model=list[Story])
def list_stories() -> list[Story]:
    return story_controller.list_stories()


@router.get("/{story_id}", response_model=Story)
def get_story(story_id: str) -> Story:
    story = story_controller.get_story(story_id)
    if story is None:
        raise HTTPException(status_code=404, detail="story not found")
    return story


@router.delete("/{story_id}", status_code=204)
def delete_story(story_id: str) -> None:
    if story_controller.get_story(story_id) is None:
        raise HTTPException(status_code=404, detail="story not found")
    story_controller.delete_story(story_id)
