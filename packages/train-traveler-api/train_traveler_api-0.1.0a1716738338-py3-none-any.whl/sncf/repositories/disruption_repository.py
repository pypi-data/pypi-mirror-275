from datetime import datetime

from sncf.connections.connection_manager import ApiConnectionManager
from sncf.repositories.repository_manager import ApiRepository

from sncf.entities.disruption_entity import DisruptionEntity, ImpactedObjectEntity, ImpactedStopsEntity
from sncf.entities.public_transport_entity import TripEntity
from sncf.entities.stop_entity import StopPointEntity

class ApiDisruptionRepository(ApiRepository):

    _connection: ApiConnectionManager
    _api: str

    def __init__(self, connection: ApiConnectionManager):
        self._connection = connection
        self._api = "coverage"
        self._route = "/disruptions"


    def find_disruption_by_id(self, disruption_id: str) -> DisruptionEntity:
        disruption_entity: DisruptionEntity

        try:
            response = self.request(endpoint="/{}".format(disruption_id))
        except Exception as error:
            raise Exception("Error: Impossible to get disruption id '{id}', {error}".format(id=disruption_id, error=error))

        disruption = response.json()["disruptions"][0]

        impacted_objects_entities = []
        impacted_object = disruption["impacted_objects"][0]
        trip_entity = TripEntity(
            id=impacted_object["pt_object"]["id"],
            name=impacted_object["pt_object"]["trip"]["name"]
        )

        impacted_stops_entitites = []
        if "impacted_stops" in impacted_object:
            for impacted_stop in impacted_object["impacted_stops"]:
                stop_point_entity = StopPointEntity(
                    id=impacted_stop["stop_point"]["id"],
                    name=impacted_stop["stop_point"]["name"],
                    label=impacted_stop["stop_point"]["label"],
                    coord={
                        "lon": impacted_stop["stop_point"]["coord"]["lon"],
                        "lat": impacted_stop["stop_point"]["coord"]["lat"]
                    },
                    stop_area=[]
                )

                if "base_departure_time" not in impacted_stop:
                    base_departure_time = None
                else:
                    base_departure_time = datetime.strptime(impacted_stop["base_departure_time"],"%H%M%S")

                if "base_arrival_time" not in impacted_stop:
                    base_arrival_time = None
                else:
                    base_arrival_time = datetime.strptime(impacted_stop["base_arrival_time"],"%H%M%S")

                if "amended_arrival_time" not in impacted_stop:
                    amended_arrival_time = None
                else:
                    amended_arrival_time = datetime.strptime(impacted_stop["amended_arrival_time"],"%H%M%S")

                if "amended_departure_time" not in impacted_stop:
                    ammended_departure_time = None
                else:
                    ammended_departure_time = datetime.strptime(impacted_stop["amended_departure_time"],"%H%M%S")


                impactedStopEntity = ImpactedStopsEntity(
                    stop_point=stop_point_entity,
                    base_arrival_time=base_arrival_time,
                    amended_arrival_time=amended_arrival_time,
                    base_departure_time=base_departure_time,
                    ammended_departure_time=ammended_departure_time,
                    departure_status=impacted_stop["departure_status"],
                    arrival_status=impacted_stop["arrival_status"],
                    cause=impacted_stop["cause"]
                )

                impacted_stops_entitites.append(impactedStopEntity)
            
            impacted_object_entity = ImpactedObjectEntity(
                public_transport=trip_entity,
                impacted_stops=impacted_stops_entitites
            )

            impacted_objects_entities.append(impacted_object_entity)

        messages = ["No message"]
        if "messages" in disruption:
            messages = [message["text"] for message in disruption["messages"] if "messages" in disruption]

        disruption_entity = DisruptionEntity(
            id=disruption["id"],
            status=disruption["status"],
            severity_effect=disruption["severity"]["effect"],
            severity_name=disruption["severity"]["name"],
            messages=messages,
            impacted_objects=impacted_objects_entities
        )

        return disruption_entity