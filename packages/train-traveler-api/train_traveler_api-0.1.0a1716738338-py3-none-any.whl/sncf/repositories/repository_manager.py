import requests
from requests.auth import HTTPBasicAuth

from sncf.connections.connection_manager import ApiConnectionManager

class ApiRepository(object):

    _connection: ApiConnectionManager
    _api: str
    _route: str
    _query_count = 0

    def __init__(self, connection: ApiConnectionManager):
        self._connection = connection

    def convert_parameters_keys_to_array(self, parameters) -> dict:
        keys_to_update = []
        for parameter, value in parameters.items():
            if type(value) is list:
                keys_to_update.append(parameter)

        for key in keys_to_update:
            parameters[key + "[]"] = parameters.pop(key)

        return parameters

    def key_validator(self, entry, keys) -> list:
        missing_keys = []

        for key in keys:
            if key not in entry:
                missing_keys.append(key)

        return missing_keys
    

    def request(self, endpoint: str, parameters: dict = {}) -> requests.Response | None:
        query = "{url}/{api}/{region}{route}{endpoint}".format(
            url=self._connection.root_url, 
            api=self._api, 
            region=self._connection.region, 
            route=self._route, 
            endpoint=endpoint
        )

        try:
            request = requests.get(query, params=parameters, auth=HTTPBasicAuth(self._connection.api_key, ''))
            ApiRepository._query_count += 1
            request.raise_for_status()

            response = request.json()
            if "error" in response:
                raise Exception(response)
            
        except requests.exceptions.HTTPError as http_error:
            raise Exception(http_error)
        
        return request if request.json else None
    
    def validate_auth(self, api) -> bool:
        query = "{url}/{api}".format(
            url=self._connection.root_url, 
            api=api, 
        )

        try:
            request = requests.get(query, auth=HTTPBasicAuth(self._connection.api_key, ''))
            ApiRepository._query_count += 1
            if not request.ok:
                return False

        except requests.exceptions.HTTPError as http_error:
            raise Exception(http_error)
        
        return True
    
        