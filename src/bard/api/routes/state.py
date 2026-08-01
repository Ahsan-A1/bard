from fastapi import APIRouter, HTTPException

from ...controllers import story_controller, world_controller
from ...entities import Checkpoint, World

router = APIRouter(prefix="/stories/{story_id}", tags=["state"])


@router.get("/checkpoints", response_model=list[Checkpoint])
def get_checkpoints(story_id: str) -> list[Checkpoint]:
    if story_controller.get_story(story_id) is None:
        raise HTTPException(status_code=404, detail="story not found")
    return world_controller.get_checkpoints(story_id)


@router.get("/world", response_model=World)
def get_world(story_id: str) -> World:
    world = world_controller.get_world(story_id)
    if world is None:
        raise HTTPException(status_code=404, detail="world not found")
    return world
