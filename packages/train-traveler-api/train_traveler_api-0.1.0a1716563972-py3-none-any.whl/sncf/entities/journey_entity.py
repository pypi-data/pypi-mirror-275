from datetime import datetime

from sncf.entities.entity_manager import Entity
from sncf.entities.stop_entity import StopEntity
from sncf.entities.stop_date_time_entity import StopDateTimeEntity
from sncf.entities.information_entity import InformationEntity

class SectionEntity(Entity):

    def __init__(
            self, 
            id: str, 
            duration: int, 
            departure_date_time: datetime, 
            scheduled_departure_date_time: datetime, 
            arrival_date_time: datetime, 
            scheduled_arrival_date_time: datetime, 
            start: StopEntity,
            end: StopEntity,
            informations: InformationEntity,
            next_stop_date_times: list[StopDateTimeEntity]):
        self.id = id
        self.duration = duration
        self.departure_date_time = departure_date_time
        self.scheduled_departure_date_time = scheduled_departure_date_time
        self.arrival_date_time = arrival_date_time
        self.scheduled_arrival_date_time = scheduled_arrival_date_time
        self.start = start
        self.end = end
        self.informations = informations
        self.next_stop_date_times = next_stop_date_times


class JourneyEntity(Entity):

    def __init__(
            self,
            duration: int, 
            departure_date_time: datetime, 
            arrival_date_time: datetime, 
            requestedDateTime: datetime,
            status: str,
            sections: list[SectionEntity]
            
    ):
        self.duration = duration
        self.departure_date_time = departure_date_time
        self.arrival_date_time = arrival_date_time
        self.requestedDateTime = requestedDateTime
        self.status = status
        self.sections = sections