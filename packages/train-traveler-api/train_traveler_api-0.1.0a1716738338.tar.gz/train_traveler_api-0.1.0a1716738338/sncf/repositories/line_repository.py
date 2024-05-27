
from sncf.connections.connection_manager import ApiConnectionManager
from sncf.repositories.repository_manager import ApiRepository

from sncf.entities.stop_entity import StopPointEntity, StopAreaEntity

class ApiLineRepository(ApiRepository):

    _connection: ApiConnectionManager
    _api: str

    def __init__(self, connection: ApiConnectionManager):
        self._connection = connection
        self._api = "coverage"
        self._route = "/lines" 

    def find_stop_points_by_line_id(self, line_id: str) -> list[StopPointEntity]:
        try:
            response = self.request(endpoint="/{}/stop_points".format(line_id))
        except Exception as error:
            print("Error: Impossible to get stop_points with line id '{line_id}', ".format(line_id=line_id), error)

        
        stop_points = response.json()["stop_points"]

        stop_points_entities = []
        for stop_point in stop_points:

            stop_area_entity = StopAreaEntity(
                id=stop_points["stop_area"]["id"],
                name=stop_point["stop_area"]["name"],
                label=stop_point["stop_area"]["label"],
                coord={
                    "lon": stop_point["stop_area"]["coord"]["lon"],
                    "lat": stop_point["stop_area"]["coord"]["lat"]
                },
                stop_points=[]
            )

            stop_point_entity = stop_point_entity(
                id=stop_point["id"],
                name=stop_point["name"],
                label=stop_point["label"],
                coord={
                    "lon": stop_point["coord"]["lon"],
                    "lat": stop_point["coord"]["lat"]
                },
                stop_area=stop_area_entity
            )

            stop_points_entities.append(stop_point_entity)

        return stop_points_entities
