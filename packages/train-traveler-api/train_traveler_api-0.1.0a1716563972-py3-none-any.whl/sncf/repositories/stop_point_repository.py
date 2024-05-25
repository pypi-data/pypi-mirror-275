from sncf.connections.connection_manager import ApiConnectionManager
from sncf.repositories.repository_manager import ApiRepository

class StopPointRepository(ApiRepository):

    _connection: ApiConnectionManager
    _api: str

    def __init__(self, connection: ApiConnectionManager):
        self._connection = connection
        self._api = "coverage"
        self._route = "/stop_points"