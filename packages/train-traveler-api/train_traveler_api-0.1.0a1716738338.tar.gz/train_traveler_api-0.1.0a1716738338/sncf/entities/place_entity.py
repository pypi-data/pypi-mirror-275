from sncf.entities.entity_manager import Entity
from sncf.entities.stop_entity import StopAreaEntity

class PlaceEntity(Entity):
    
    def __init__(self, id: str, name: str, embedded_type: str):
        self.id = id
        self.name = name
        self.embedded_type = embedded_type


class PlaceAreaEntity(PlaceEntity):

    def __init__(self, id: str, name: str, stop_area: StopAreaEntity):
        self.embedded_type = "stop_area"
        super().__init__(id, name, self.embedded_type)

        self.stop_area = stop_area
