from datetime import datetime

from sncf.entities.entity_manager import Entity


class LineEntity(Entity):

    def __init__(self, id: str, name: str, code: str, color: str, opening_time: datetime, closing_time: datetime):
        self.id = id
        self.name = name
        self.code = code
        self.color = color
        self.opening_time = opening_time.strftime("%H:%M:%S")
        self.closing_time = closing_time.strftime("%H:%M:%S")