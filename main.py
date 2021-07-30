#!/usr/bin/env python3
import tcod

from game_map import GameMap
from engine import Engine
from input_handlers import EventHandler
from entity import Entity

def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 50

    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))

    game_map = GameMap(map_width, map_height)

    entities = { player }

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Avalon v0.01a",
        vsync=True,
    ) as context:
        root_console = tcod.Console(screen_width, screen_height, order="F")

        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()