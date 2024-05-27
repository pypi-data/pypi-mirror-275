from datetime import datetime

from sncf.entities.entity_manager import Entity
from sncf.entities.stop_entity import StopPointEntity

class StopDateTimeEntity(Entity):

    def __init__(self, 
                 scheduled_departure_date_time: datetime, 
                 departure_date_time: datetime, 
                 scheduled_arrival_date_time: datetime, 
                 arrival_date_time: datetime,
                 stop_point: StopPointEntity 
                
    ):
        self.scheduled_departure_date_time = scheduled_departure_date_time
        self.departure_date_time = departure_date_time
        self.scheduled_arrival_date_time = scheduled_arrival_date_time
        self.arrival_date_time = arrival_date_time
        self.stop_point = stop_point