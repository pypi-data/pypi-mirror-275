from sncf.services.service_manager import ServiceManager
from sncf.entities.stop_entity import StopAreaEntity

from sncf.models.area_model import Area

class AreaService(ServiceManager):

    def __init__(self):
        pass

    def create_area(self, stop_area: StopAreaEntity) -> Area:
        return Area(
            id=stop_area.id,
            name=stop_area.name,
            label=stop_area.label,
            coord=stop_area.coord
        )