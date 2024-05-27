from sncf.entities.entity_manager import Entity

class PublicTransportEntity(Entity):

    def __init__(self, id: str, embedded_type: str):
        self.id = id
        self.embedded_type = embedded_type


class TripEntity(PublicTransportEntity):
    
    def __init__(self, id: str, name: str):
        self.embedded_type = "trip"
        super().__init__(id, self.embedded_type)

        self.name = name


