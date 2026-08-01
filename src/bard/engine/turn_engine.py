from ..entities import Turn


class TurnEngine:
    def play_turn(self, story_id: str, action: str, generate_image: bool) -> Turn:
        raise NotImplementedError
