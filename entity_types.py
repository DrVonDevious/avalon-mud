error_entity = None

from entity import Entity

error_entity = Entity(
    char="X",
    color=(255, 0, 0),
    name="Error",
    entity_id="ffff",
)

player = Entity(
    char="@",
    color=(255, 255, 255),
    name="Sam",
    entity_id="0001",
)

pine_tree = Entity(
    char="t",
    color=(150, 200, 0),
    name="Pine Tree",
    entity_id="0002",
)

types = [
    { "entity_id": error_entity.entity_id, "entity": error_entity },
    { "entity_id": player.entity_id, "entity": player },
    { "entity_id": pine_tree.entity_id, "entity": pine_tree }
]
