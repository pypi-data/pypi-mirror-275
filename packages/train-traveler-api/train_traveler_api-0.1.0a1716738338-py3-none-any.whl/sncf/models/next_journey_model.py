from sncf.models.area_model import Area
from sncf.models.journey_model import Journey

class NextJourney(object):

    def __init__(self, start: Area, end: Area, journeys: list[Journey]):
        self.start = start
        self.end = end
        self.journeys = journeys