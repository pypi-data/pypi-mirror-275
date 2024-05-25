from __future__ import annotations

from sncf.entities.entity_manager import Entity

class StopEntity(Entity):
    def __init__(self, id: str, name: str, label: str, coord: dict):
        self.id = id
        self.name = name
        self.label = label
        self.coord = coord



class StopAreaEntity(StopEntity):

    def __init__(self, id: str, name: str, label: str, coord: dict, stop_points: list[StopPointEntity]):
        super().__init__(id, name, label, coord)
        self.stop_points = stop_points


class StopPointEntity(StopEntity):

    def __init__(self, id: str, name: str, label: str, coord: dict, stop_area: StopAreaEntity):
        super().__init__(id, name, label, coord)
        self.stop_area = stop_area
