from sncf.services.service_manager import ServiceManager
from sncf.repositories.repository_manager import ApiRepository

class InfoService(ServiceManager):

    def __init__(self, repository_manager: ApiRepository):
          self.repository_manager = repository_manager

    def validate_coverage_auth(self):
        return self.repository_manager.validate_auth(api="coverage")
