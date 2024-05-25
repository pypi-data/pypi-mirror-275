from sncf.entities.journey_entity import JourneyEntity
from sncf.entities.disruption_entity import DisruptionEntity

class Journey(object):

    def __init__(self, journey: JourneyEntity, disruptions: list[DisruptionEntity]):
        self.journey = journey
        self.disruptions = disruptions