from sncf.connections.connection_manager import ApiConnectionManager
from sncf.repositories.repository_manager import ApiRepository

from sncf.entities.place_entity import PlaceAreaEntity
from sncf.entities.stop_entity import StopAreaEntity

class ApiPlaceRepository(ApiRepository):

    _connection: ApiConnectionManager
    _api: str

    def __init__(self, connection: ApiConnectionManager):
        self._connection = connection
        self._api = "coverage"
        self._route = "/places"

    def find_areas_from_places(self, search: str) -> list[PlaceAreaEntity]:
        try:
            response = self.request(endpoint="", parameters={"q": search, "disable_geojson": True, "type[]": ["stop_area"]})
        except Exception as error:
            print("Error: Impossible to get places from /places endpoint for '{search}'".format(search=search), error)

        places = response.json()["places"]


        places_entities = []

        for place in places:

            stop_area=StopAreaEntity(
                id=place["stop_area"]["id"],
                name=place["stop_area"]["name"],
                label=place["stop_area"]["label"],
                coord={
                    "lon": place["stop_area"]["coord"]["lon"],
                    "lat": place["stop_area"]["coord"]["lat"]
                },
                stop_points=[]
            )

            place_entity = PlaceAreaEntity(
                id=place["id"],
                name=place["name"],
                stop_area=stop_area
            )

            places_entities.append(place_entity)
        
        return places_entities