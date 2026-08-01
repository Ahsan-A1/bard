from ..entities import Turn
from ..storage import store


class TurnController:
    def play_turn(self, story_id: str, action: str, generate_image: bool) -> Turn:
        raise NotImplementedError

    def list_turns(self, story_id: str) -> list[Turn]:
        return [t for t in store.turns.all() if t.story_id == story_id]

    def get_turn(self, story_id: str, turn_id: str) -> Turn | None:
        turn = store.turns.get(turn_id)
        if turn is None or turn.story_id != story_id:
            return None
        return turn

    def get_turn_image(self, story_id: str, turn_id: str) -> str | None:
        raise NotImplementedError

    def synthesize_turn_tts(self, story_id: str, turn_id: str) -> bytes:
        raise NotImplementedError
