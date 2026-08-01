from fastapi import APIRouter, HTTPException

from ...controllers import character_controller, story_controller
from ...entities import Character

router = APIRouter(prefix="/stories/{story_id}/characters", tags=["characters"])


@router.get("", response_model=list[Character])
def list_characters(story_id: str) -> list[Character]:
    if story_controller.get_story(story_id) is None:
        raise HTTPException(status_code=404, detail="story not found")
    return character_controller.list_characters(story_id)


@router.get("/{character_id}", response_model=Character)
def get_character(story_id: str, character_id: str) -> Character:
    character = character_controller.get_character(story_id, character_id)
    if character is None:
        raise HTTPException(status_code=404, detail="character not found")
    return character
