from sncf.connections.connection_manager import ApiConnectionManager
from sncf.repositories.repository_manager import ApiRepository

from sncf.entities.link_entity import LinkEntity

class ApiLinkRepository(ApiRepository):

    _connection: ApiConnectionManager
    _api: str

    def __init__(self, connection: ApiConnectionManager):
        self._connection = connection
        self._api = ""
        self._route = ""


    def find_links(self, **kwargs) -> list[LinkEntity]:
        parameters = {}
        parameters.update(kwargs)

        parameters = self.convert_parameters_keys_to_array(parameters)

        try:
            response = self.request(endpoint="", parameters=parameters)
            print(response)
        except Exception as error:
            raise Exception("Error: Impossible to get links', {error}".format(error=error)) 
            
        
        links = response.json()["links"]
        
        link_entities: list[LinkEntity] = [] 
        for link in links:
            link_entities.append(
                LinkEntity(
                    href=link["href"],
                    templated=link["templated"],
                    rel=link["rel"],
                    type=link["type"],
                    title=link["title"]
                )
            )

        return link_entities