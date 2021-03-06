from typing import Iterable, Any


from tcod.context import Context
from tcod.console import Console
from tcod.map import compute_fov

from render_functions import render_hp_bar, render_map_editor
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


class Engine:
    def __init__(
        self,
        event_handler: EventHandler,
        game_map: GameMap,
        player: Entity
    ):
        self.event_handler = event_handler
        self.game_map = game_map
        self.player = player
        self.update_fov()

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(self, self.player)

            self.update_fov()

    def update_fov(self) -> None:
        self.game_map.visible[:] = compute_fov(
            self.game_map.tiles["transparent"],
            (self.player.x, self.player.y),
            radius=24
        );

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        render_hp_bar(
            console=console,
            current_value=60,
            maximum_value=100,
            total_width=20
        )

        render_map_editor(console)

        context.present(console)

        console.clear()
