from ..entities import Turn


class TTSEngine:
    def synthesize_turn(self, turn: Turn) -> bytes:
        raise NotImplementedError

    def assign_voice(self, character_id: str) -> str:
        raise NotImplementedError
