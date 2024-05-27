from __future__ import annotations
from datetime import datetime

from sncf.entities.entity_manager import Entity

from sncf.entities.public_transport_entity import PublicTransportEntity
from sncf.entities.stop_entity import StopPointEntity

class DisruptionEntity(Entity):
    
    def __init__(self, id: str, status: str, severity_effect: str, severity_name: str, messages: list, impacted_objects: list[ImpactedObjectEntity]):
        self.id = id
        self.status = status
        self.severity_effect = severity_effect
        self.severity_name = severity_name
        self.messages = messages
        self.impacted_objects = impacted_objects


class ImpactedObjectEntity(Entity):
    def __init__(self, public_transport: PublicTransportEntity, impacted_stops: list[ImpactedStopsEntity]):
        self.public_transport = public_transport
        self.impacted_stops = impacted_stops
        

class ImpactedStopsEntity(Entity):
    def __init__(
            self, 
            stop_point: StopPointEntity, 
            base_arrival_time: datetime, 
            amended_arrival_time: datetime, 
            base_departure_time: datetime, 
            ammended_departure_time: datetime,
            departure_status: str,
            arrival_status: str,
            cause: str
        ):
        self.stop_point = stop_point
        self.base_arrival_time = base_arrival_time
        self.amended_arrival_time = amended_arrival_time
        self.base_departure_time = base_departure_time
        self.ammended_departure_time = ammended_departure_time
        self.departure_status = departure_status
        self.arrival_status = arrival_status
        self.cause = cause