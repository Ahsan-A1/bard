from .character_controller import CharacterController
from .story_controller import StoryController
from .turn_controller import TurnController
from .world_controller import WorldController

story_controller = StoryController()
turn_controller = TurnController()
character_controller = CharacterController()
world_controller = WorldController()

__all__ = [
    "CharacterController",
    "StoryController",
    "TurnController",
    "WorldController",
    "character_controller",
    "story_controller",
    "turn_controller",
    "world_controller",
]
