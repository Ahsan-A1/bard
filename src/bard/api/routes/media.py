from fastapi import APIRouter, HTTPException, Response

from ...controllers import turn_controller

router = APIRouter(prefix="/stories/{story_id}/turns/{turn_id}", tags=["media"])


@router.get("/image")
def get_turn_image(story_id: str, turn_id: str) -> Response:
    if turn_controller.get_turn(story_id, turn_id) is None:
        raise HTTPException(status_code=404, detail="turn not found")
    try:
        turn_controller.get_turn_image(story_id, turn_id)
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail="image not implemented") from e
    return Response(status_code=204)


@router.post("/tts")
def synthesize_turn_tts(story_id: str, turn_id: str) -> Response:
    if turn_controller.get_turn(story_id, turn_id) is None:
        raise HTTPException(status_code=404, detail="turn not found")
    try:
        audio = turn_controller.synthesize_turn_tts(story_id, turn_id)
    except NotImplementedError as e:
        raise HTTPException(status_code=501, detail="tts not implemented") from e
    return Response(content=audio, media_type="audio/mpeg")
