from sncf.entities.entity_manager import Entity

class InformationEntity(Entity):

    def __init__(self, commercialMode: str, network: str, direction: str, label: str, color: str, code: str, name: str, physical_mode: str, trip_short_name: str, disruptions_ids: list):
        self.commercialMode = commercialMode
        self.network = network
        self.direction = direction
        self.label = label
        self.color = color
        self.code = code 
        self.name = name
        self.physical_mode = physical_mode
        self.trip_short_name = trip_short_name
        self.disruptions_ids = disruptions_ids