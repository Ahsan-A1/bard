from ..entities import Character
from ..storage import store


class CharacterController:
    def list_characters(self, story_id: str) -> list[Character]:
        return [c for c in store.characters.all() if c.story_id == story_id]

    def get_character(self, story_id: str, character_id: str) -> Character | None:
        character = store.characters.get(character_id)
        if character is None or character.story_id != story_id:
            return None
        return character
