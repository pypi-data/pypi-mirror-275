from datetime import datetime

from sncf.connections.connection_manager import ApiConnectionManager
from sncf.repositories.repository_manager import ApiRepository

from sncf.entities.journey_entity import JourneyEntity, SectionEntity
from sncf.entities.stop_entity import StopPointEntity
from sncf.entities.information_entity import InformationEntity
from sncf.entities.stop_date_time_entity import StopDateTimeEntity

class ApiJourneyRepository(ApiRepository):

    _connection: ApiConnectionManager
    _api: str

    def __init__(self, connection: ApiConnectionManager):
        self._connection = connection
        self._api = "coverage"
        self._route = "/journeys"


    def find_journeys(self, start: str, end: str, **kwargs) -> list[JourneyEntity]:
        parameters = {"from": start, "to": end}
        parameters.update(kwargs)

        parameters = self.convert_parameters_keys_to_array(parameters)

        try:
            response = self.request(endpoint="", parameters=parameters)
        except Exception as error:
            if error.args[0]["error"]["id"] == "no_solution":
                return []
            else:
                raise Exception("Error: Impossible to get journey from '{start}' to '{end}', {error}".format(start=start, end=end, error=error))
        
        journeys = response.json()["journeys"]

        journeys_entities = []
        for journey in journeys:  

            sections_entities = []
            for section in journey["sections"]:
                
                if section["type"] != "public_transport":
                    continue
                
                # In some cases, to and from are equals and informations are still retrieved, so we skip it
                if section["to"]["stop_point"]["stop_area"]["id"] == section["from"]["stop_point"]["stop_area"]["id"]:
                    continue                

                informations = section["display_informations"]

                disruptions_ids = []
                for link in informations["links"]:
                    if link["type"] == "disruption":
                        disruptions_ids.append(link["id"])

                information_entity = InformationEntity(
                    commercialMode=informations["commercial_mode"],
                    network=informations["network"],
                    direction=informations["direction"],
                    label=informations["label"],
                    code=informations["code"],
                    color=informations["color"],
                    name=informations["name"],
                    physical_mode=informations["physical_mode"],
                    trip_short_name=informations["trip_short_name"],
                    disruptions_ids=disruptions_ids
                )

                next_stop_date_times_entities = []
                next_stop_date_times = section["stop_date_times"]

                for stop_date_time in next_stop_date_times:

                    departure_date_time = datetime.strptime(stop_date_time["departure_date_time"],"%Y%m%dT%H%M%S")
                    arrival_date_time = datetime.strptime(stop_date_time["arrival_date_time"],"%Y%m%dT%H%M%S")

                    # In case of modified services, base_departure_date_time and base_arrival_date_time cannot be filled
                    if "base_departure_date_time" not in stop_date_time:
                        scheduled_departure_date_time = departure_date_time
                    else:
                        scheduled_departure_date_time = datetime.strptime(stop_date_time["base_departure_date_time"],"%Y%m%dT%H%M%S")

                    if "base_arrival_date_time" not in stop_date_time:
                        scheduled_arrival_date_time = arrival_date_time
                    else:
                        scheduled_arrival_date_time=datetime.strptime(stop_date_time["base_arrival_date_time"],"%Y%m%dT%H%M%S")

                    stop_date_time_entity = StopDateTimeEntity(
                        scheduled_departure_date_time=scheduled_departure_date_time,
                        departure_date_time=departure_date_time,
                        scheduled_arrival_date_time=scheduled_arrival_date_time,
                        arrival_date_time=arrival_date_time,
                        stop_point=StopPointEntity(
                            id=stop_date_time["stop_point"]["id"],
                            name=stop_date_time["stop_point"]["name"],
                            label=stop_date_time["stop_point"]["label"],
                            coord={
                                "lon": stop_date_time["stop_point"]["coord"]["lon"],
                                "lat": stop_date_time["stop_point"]["coord"]["lat"]
                            },
                            stop_area=[]
                        )
                    )
                    next_stop_date_times_entities.append(stop_date_time_entity)

                if section["from"]["embedded_type"] == "stop_point":

                    start_point = section["from"]["stop_point"]

                    start_stop_entity = StopPointEntity(
                        id=start_point["id"],
                        name=start_point["name"],
                        label=start_point["label"],
                        coord={
                            "lon": start_point["coord"]["lon"],
                            "lat": start_point["coord"]["lat"]
                        },
                        stop_area=[]
                    )
                else:
                    start_stop_entity = None

                
                if section["to"]["embedded_type"] == "stop_point":

                    end_point = section["to"]["stop_point"]

                    end_stop_entity = StopPointEntity(
                        id=end_point["id"],
                        name=end_point["name"],
                        label=end_point["label"],
                        coord={
                            "lon": end_point["coord"]["lon"],
                            "lat": end_point["coord"]["lat"]
                        },
                        stop_area=[]
                    )
                else:
                    end_stop_entity = None

                
                departure_date_time = datetime.strptime(section["departure_date_time"],"%Y%m%dT%H%M%S")
                arrival_date_time = datetime.strptime(section["arrival_date_time"],"%Y%m%dT%H%M%S")

                # In case of modified services, base_departure_date_time and base_arrival_date_time cannot be filled
                if "base_departure_date_time" not in stop_date_time:
                    scheduled_departure_date_time = departure_date_time
                else:
                    scheduled_departure_date_time = datetime.strptime(section["base_departure_date_time"],"%Y%m%dT%H%M%S")

                if "base_arrival_date_time" not in stop_date_time:
                    scheduled_arrival_date_time = arrival_date_time
                else:                    
                    scheduled_arrival_date_time = datetime.strptime(section["base_arrival_date_time"],"%Y%m%dT%H%M%S")

                section_entity = SectionEntity(
                    id=section["id"],
                    duration=section["duration"],
                    departure_date_time=departure_date_time,
                    scheduled_departure_date_time=scheduled_departure_date_time,
                    arrival_date_time=arrival_date_time,
                    scheduled_arrival_date_time=scheduled_arrival_date_time,
                    start=start_stop_entity,
                    end=end_stop_entity,
                    informations=information_entity,
                    next_stop_date_times=next_stop_date_times_entities
                )
                
                sections_entities.append(section_entity)


            journey_entity = JourneyEntity(
                duration=journey["duration"],
                departure_date_time=datetime.strptime(journey["departure_date_time"],"%Y%m%dT%H%M%S"),
                arrival_date_time=datetime.strptime(journey["arrival_date_time"],"%Y%m%dT%H%M%S"),
                requestedDateTime=datetime.strptime(journey["requested_date_time"],"%Y%m%dT%H%M%S"),
                status=journey["status"],
                sections=sections_entities
            )

            journeys_entities.append(journey_entity)

        return journeys_entities

