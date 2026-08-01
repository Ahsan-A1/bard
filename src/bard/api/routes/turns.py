from fastapi import APIRouter, HTTPException

from ...controllers import story_controller, turn_controller
from ...entities import Turn
from ..schemas import PlayTurnRequest

router = APIRouter(prefix="/stories/{story_id}/turns", tags=["turns"])


@router.post("", response_model=Turn, status_code=201)
def play_turn(story_id: str, body: PlayTurnRequest) -> Turn:
    if story_controller.get_story(story_id) is None:
        raise HTTPException(status_code=404, detail="story not found")
    try:
        return turn_controller.play_turn(story_id, body.action, body.generate_image)
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail="play_turn not implemented") from e


@router.get("", response_model=list[Turn])
def list_turns(story_id: str) -> list[Turn]:
    if story_controller.get_story(story_id) is None:
        raise HTTPException(status_code=404, detail="story not found")
    return turn_controller.list_turns(story_id)
