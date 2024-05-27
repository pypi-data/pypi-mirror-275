from datetime import datetime, timedelta

from sncf.services.service_manager import ServiceManager

from sncf.repositories.stop_area_repository import ApiStopAreaRepository
from sncf.repositories.journey_repository import ApiJourneyRepository
from sncf.repositories.disruption_repository import ApiDisruptionRepository

from sncf.entities.journey_entity import JourneyEntity
from sncf.entities.disruption_entity import DisruptionEntity

from sncf.models.next_journey_model import NextJourney
from sncf.models.area_model import Area
from sncf.models.journey_model import Journey

class JourneyService(ServiceManager):

    def __init__(self, 
                 stop_area_repository: ApiStopAreaRepository, 
                 journey_repository: ApiJourneyRepository,
                 disruption_repository: ApiDisruptionRepository
                 ):
          self.stop_area_repository = stop_area_repository
          self.journey_repository = journey_repository
          self.disruption_repository = disruption_repository

    def __get_common_lines_between_areas(self, start_area_id: str, end_area_id: str) -> list:
        try:
            linesInStartArea = self.stop_area_repository.find_lines_by_stop_area_id(start_area_id)
            linesInEndArea = self.stop_area_repository.find_lines_by_stop_area_id(end_area_id)
        except Exception as error:
                raise Exception("Error: Impossible to find lines from area id '{start_id}' and '{end_id}'".format(start_id=start_area_id, end_id=end_area_id))

        return [ line for line in linesInStartArea if any(line.id == endLine.id for endLine in linesInEndArea) ]
    

    def __get_journeys_from_entities(self, journeys_entities: list[JourneyEntity]) -> list[Journey]:
        journeys: list[Journey] = []
        for journey in journeys_entities:
            disruptions: list[DisruptionEntity] = []
            for section in journey.sections:
                for disruption_id in section.informations.disruptions_ids:
                    try:
                        disruption = self.disruption_repository.find_disruption_by_id(disruption_id)
                    except Exception:
                            raise
                    disruptions.append(disruption)
            journeys.append(Journey(
                    journey, disruptions
            ))
        return journeys



    def get_last_direct_journey(self, start_area: Area, end_area: Area) -> NextJourney:
            try:
                lines = self.__get_common_lines_between_areas(start_area.id, end_area.id)
            except Exception as error:
                 raise

            lines_journeys: list[JourneyEntity] = []
            for line in lines:
                try:
                    start_stop_point = self.stop_area_repository.find_area_stop_point_by_line_id(start_area.id, line.id)
                    end_stop_point = self.stop_area_repository.find_area_stop_point_by_line_id(end_area.id, line.id)


                    last_journeys = self.journey_repository.find_journeys(
                        start_stop_point.id, 
                        end_stop_point.id, 
                        allowed_id=[line.id], 
                        max_nb_transfers=0, 
                        datetime=datetime.today().strftime("%Y%m%d")+"T235959", 
                        datetime_represents="arrival",
                        data_freshness="realtime"
                    )

                    # In order to check the last journey, we need to fetch the first journey that starts the day after
                    # Then we take the next_journey - 1

                    if len(last_journeys) > 0:
                         
                        next_journeys = self.journey_repository.find_journeys(
                            start_stop_point.id, 
                            end_stop_point.id, 
                            allowed_id=[line.id], 
                            max_nb_transfers=0, 
                            datetime=last_journeys[0].departure_date_time + timedelta(seconds=1), 
                            datetime_represents="departure",
                            data_freshness="realtime"
                        )

                        

                        while len(next_journeys) > 0 and next_journeys[0].departure_date_time.date() == datetime.today().date():
                            last_journeys = next_journeys

                            next_journeys = self.journey_repository.find_journeys(
                                start_stop_point.id, 
                                end_stop_point.id, 
                                allowed_id=[line.id], 
                                max_nb_transfers=0, 
                                datetime=next_journeys[0].departure_date_time + timedelta(seconds=1), 
                                datetime_represents="departure",
                                data_freshness="realtime"
                            )

                    lines_journeys.extend(
                        last_journeys
                    )
                    
                except Exception as error:
                     raise
            
            lines_journeys.sort(key=lambda x: x.departure_date_time, reverse=True)

            if len(lines_journeys) > 0:
                lines_journeys = [lines_journeys[0]]

            journeys = self.__get_journeys_from_entities(lines_journeys)

            next_journey =  NextJourney(
                start_area,
                end_area,
                journeys
            )
            
            return next_journey
            

    def get_direct_journeys(self, start_area: Area, end_area: Area, count=0) -> NextJourney:

            try:
                lines = self.__get_common_lines_between_areas(start_area.id, end_area.id)
            except Exception as error:
                 raise

            lines_journeys: list[JourneyEntity] = []
            for line in lines:
                try:
                    start_stop_point = self.stop_area_repository.find_area_stop_point_by_line_id(start_area.id, line.id)
                    end_stop_point = self.stop_area_repository.find_area_stop_point_by_line_id(end_area.id, line.id)

                    lines_journeys.extend(
                        self.journey_repository.find_journeys(start_stop_point.id, end_stop_point.id, allowed_id=[line.id], max_nb_transfers=0, count=count, data_freshness="realtime")
                    )
                    
                except Exception as error:
                     raise
            
            lines_journeys.sort(key=lambda x: x.departure_date_time)
            lines_journeys = lines_journeys[0:count]
            
            journeys = self.__get_journeys_from_entities(lines_journeys)

            next_journey =  NextJourney(
                start_area,
                end_area,
                journeys
            )
            
            return next_journey





