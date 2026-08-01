from ..config import settings
from ..entities import Character, Story, Turn, World
from .json_repository import JsonRepository


class Store:
    def __init__(self) -> None:
        data_dir = settings.data_dir
        self.stories: JsonRepository[Story] = JsonRepository(
            data_dir / "stories.json", Story
        )
        self.turns: JsonRepository[Turn] = JsonRepository(
            data_dir / "turns.json", Turn
        )
        self.characters: JsonRepository[Character] = JsonRepository(
            data_dir / "characters.json", Character
        )
        self.worlds: JsonRepository[World] = JsonRepository(
            data_dir / "worlds.json", World, pk_getter=lambda w: w.story_id
        )

    def load_all(self) -> None:
        self.stories.load()
        self.turns.load()
        self.characters.load()
        self.worlds.load()


store = Store()
