from typing import Tuple

class Entity:
    """
    An object to represent any interactable thing in the game
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    # Move entity by a given amount
    def move(self, dx: int, dy: int) -> None:
        self.x += dx
        self.y += dy
