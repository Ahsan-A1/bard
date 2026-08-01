from ..entities import Checkpoint, World
from ..storage import store


class WorldController:
    def get_world(self, story_id: str) -> World | None:
        return store.worlds.get(story_id)

    def get_checkpoints(self, story_id: str) -> list[Checkpoint]:
        story = store.stories.get(story_id)
        return story.checkpoints if story else []
