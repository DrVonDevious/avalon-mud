from __future__ import annotations

import numpy as np  # type: ignore
import json
from tcod.console import Console
from typing import Iterable, TYPE_CHECKING

import tile_types
import entity_types

if TYPE_CHECKING:
    from entity import Entity


class GameMap:
    def __init__(self, width: int, height: int, player: Entity, entities: Iterable[Entity] = ()):
        self.width, self.height = width, height
        self.player = player
        self.player.x = int(width / 2)
        self.player.y = int(height / 2)
        self.entities = set(entities)
        self.tiles = np.full((width, height), fill_value=tile_types.void_floor, order="F")
        self.visible = np.full((width, height), fill_value=False, order="F")
        self.explored = np.full((width, height), fill_value=False, order="F")

        # Reads map file and exports it as a 2D array
        with open("overworld_map.json", "r") as file:
            map_data = json.load(file)

        # Checks if a given tile_id in the map has a corresponding tile in tile_types
        def find_tile(tile_id):
            for tile in tile_types.types:
                if tile.get("tile_id") == tile_id:
                    return tile["tile"]

        # Checks if a given entity_id in the map has a corresponding entity in entity_types
        def find_entity(entity_id):
            for entity in entity_types.types:
                if entity.get("entity_id") == entity_id:
                    return entity["entity"]

        # Goes through each tile and gives it a tile_type based on it's ID
        # If it can't find one it gives it and error_tile type
        for y, row in enumerate(map_data["tiles"]):
            for x, tile_id in enumerate(row):
                found_tile = find_tile(tile_id)
                self.tiles[x][y] = found_tile if found_tile else tile_types.error_tile

        for y, row in enumerate(map_data["entities"]):
            for x, entity_id in enumerate(row):
                found_entity = find_entity(entity_id)

                if (found_entity):
                    found_entity.spawn(self, x, y)

        for entity in self.entities:
            print(entity.name)

    def in_bounds(self, x: int, y: int) -> bool:
        """
        Return True if x and y are inside of the bounds of this map
        """
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        """
        Renders the map
        """
        console.tiles_rgb[0: self.width, 0: self.height] = self.tiles["light"]

        for entity in self.entities:
            # Only print entities that are in the FOV
            if self.visible[entity.x, entity.y]:
                console.print(x=entity.x, y=entity.y, string=entity.char, fg=entity.color)

        # FOV
        # console.tiles_rgb[0:self.width, 0:self.height] = np.select(
        #     condlist=[self.visible, self.explored],
        #     choicelist=[self.tiles["light"], self.tiles["dark"]],
        #     default=tile_types.SHROUD
        # );
