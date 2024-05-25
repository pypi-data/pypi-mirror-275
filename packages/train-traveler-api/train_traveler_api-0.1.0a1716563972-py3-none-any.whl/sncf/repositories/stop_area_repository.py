from datetime import datetime

from sncf.connections.connection_manager import ApiConnectionManager
from sncf.repositories.repository_manager import ApiRepository

from sncf.entities.stop_entity import StopAreaEntity, StopPointEntity
from sncf.entities.line_entity import LineEntity

class ApiStopAreaRepository(ApiRepository):
    
    _connection: ApiConnectionManager
    _api: str

    def __init__(self, connection: ApiConnectionManager):
        self._connection = connection
        self._api = "coverage"
        self._route = "/stop_areas"

    def find_stop_area_by_id(self, stop_area_id: str) -> StopAreaEntity:
        try:
            response = self.request(endpoint="/{}".format(stop_area_id))
        except Exception as error:
            print("Error: Impossible to get stop_area with id '{stop_area_id}', ".format(stop_area_id=stop_area_id), error)

        stop_area = response.json()["stop_areas"][0]

        stop_area=StopAreaEntity(
            id=stop_area["id"],
            name=stop_area["name"],
            label=stop_area["label"],
            coord={
                "lon": stop_area["coord"]["lon"],
                "lat": stop_area["coord"]["lat"]
            },
            stop_points=[]
        )
        
        return stop_area
    

    def find_area_stop_point_by_line_id(self, stop_area_id: str, line_id: str) -> StopPointEntity:
        try:
            response = self.request(endpoint="/{stop_area_id}/lines/{line_id}/stop_points".format(stop_area_id=stop_area_id, line_id=line_id))
        except Exception as error:
            print("Error: Impossible to get stop_points with stop_area id '{stop_area_id}' and line '{line_id}', ".format(stop_area_id=stop_area_id), error)

        stop_point = response.json()["stop_points"][0]

        stop_point_entity = StopPointEntity(
            id=stop_point["id"],
            name=stop_point["name"],
            label=stop_point["label"],
            coord={
                    "lon": stop_point["coord"]["lon"],
                    "lat": stop_point["coord"]["lat"]
            },
            stop_area=[]
        )

        return stop_point_entity

    def find_lines_by_stop_area_id(self, stop_area_id: str) -> list[LineEntity]:
        try:
            response = self.request(endpoint="/{}/lines".format(stop_area_id), parameters={"count": 200})
        except Exception as error:
            print("Error: Impossible to get lines with stop_area id '{stop_area_id}', ".format(stop_area_id=stop_area_id), error)

        lines = response.json()["lines"]
        
        lines_entities = []
        for line in lines:

            missing_keys = self.key_validator(line, ["id", "name", "code", "color", "opening_time", "closing_time"])

            if len(missing_keys) > 0:
                for key in missing_keys:
                    if key in ["opening_time", "closing_time"]:
                        line[key] = "000000"
                    elif key in ["id", "name"]:
                        raise Exception("Error: id or name is missing for line in stop_area {stop_area_id}".format(stop_area_id=stop_area_id))
                    else:
                        line[key] = ""
                    

            line_entity = LineEntity(
                id=line["id"],
                name=line["name"],
                code=line["code"],
                color=line["color"],
                opening_time=datetime.strptime(line["opening_time"], "%H%M%S"),
                closing_time=datetime.strptime(line["closing_time"], "%H%M%S")
            )

            lines_entities.append(line_entity)
        
        return lines_entities