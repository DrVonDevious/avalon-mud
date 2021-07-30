import numpy as np  # type: ignore
import json
from tcod.console import Console

import tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height
        self.tiles = np.full((width, height), fill_value=tile_types.void_floor, order="F")

        # Reads map file and exports it as a 2D array
        with open("overworld_map.json", "r") as file:
            map_data = json.load(file)

        # Checks if a given tile_id in the map has a corresponding tile in tile_types
        def find_tile(tile_id):
            for tile in tile_types.types:
                if tile.get("tile_id") == tile_id:
                    return tile["tile"]

        # Goes through each tile and gives it a tile_type based on it's ID
        # If it can't find one it gives it and error_tile type
        for y, row in enumerate(map_data["data"]):
            for x, tile_id in enumerate(row):
                found_tile = find_tile(tile_id)
                self.tiles[x][y] = found_tile if found_tile else tile_types.error_tile

    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.tiles_rgb[0:self.width, 0:self.height] = self.tiles["dark"]
