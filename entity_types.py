import colors
from entity import Entity

error_entity = Entity(
    char="X",
    color=colors.red,
    name="<Unknown Entity>",
    entity_id="ffff",
)

player = Entity(
    char="@",
    color=colors.white,
    name="Sam",
    entity_id="0001",
)

pine_tree = Entity(
    char="t",
    color=colors.green,
    name="Pine Tree",
    entity_id="0002",
)

types = [
    { "entity_id": error_entity.entity_id, "entity": error_entity },
    { "entity_id": player.entity_id, "entity": player },
    { "entity_id": pine_tree.entity_id, "entity": pine_tree }
]
