from ..entities import Story
from ..storage import store


class StoryController:
    def create_story(self, base_prompt: str) -> Story:
        raise NotImplementedError

    def list_stories(self) -> list[Story]:
        return store.stories.all()

    def get_story(self, story_id: str) -> Story | None:
        return store.stories.get(story_id)

    def delete_story(self, story_id: str) -> None:
        for turn in [t for t in store.turns.all() if t.story_id == story_id]:
            store.turns.delete(turn.id)
        for character in [c for c in store.characters.all() if c.story_id == story_id]:
            store.characters.delete(character.id)
        store.worlds.delete(story_id)
        store.stories.delete(story_id)
