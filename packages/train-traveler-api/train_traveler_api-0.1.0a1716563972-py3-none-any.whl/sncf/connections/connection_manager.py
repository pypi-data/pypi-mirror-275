class ApiConnectionManager(object):

    api_key: str
    root_url: str
    region: str

    def __init__(self, url, api_key, region):
        
        self.api_key = api_key
        self.root_url = url
        self.region = region