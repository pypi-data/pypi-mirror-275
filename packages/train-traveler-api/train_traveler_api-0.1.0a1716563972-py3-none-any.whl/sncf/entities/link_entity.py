from sncf.entities.entity_manager import Entity


class LinkEntity(Entity):

    def __init__(self, href: str, templated: str, rel: str, type: str, title: str):
        self.href = href
        self.templated = templated
        self.rel = rel
        self.type = type
        self.title = title