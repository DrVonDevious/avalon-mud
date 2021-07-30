from __future__ import annotations

import copy
from typing import Tuple, TypeVar, TYPE_CHECKING

if TYPE_CHECKING:
    from game_map import GameMap

T = TypeVar("T", bound="Entity")

class Entity:
    """
    An object to represent any interactable thing in the game
    """
    def __init__(
            self,
            x: int = 0,
            y: int = 0,
            char: str = "?",
            color: Tuple[int, int, int] = (255, 255, 255),
            name: str = "<Unmamed>",
            entity_id: str = "<No ID>",
    ):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.entity_id = entity_id

    # Move entity by a given amount
    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy

    def spawn(self: T, gamemap: GameMap, x: int, y: int) -> T:
        """Spawn a copy of this instance at the given location."""
        clone = copy.deepcopy(self)
        clone.x = x
        clone.y = y
        gamemap.entities.add(clone)
        return clone
