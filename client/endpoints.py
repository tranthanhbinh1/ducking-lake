from enum import Enum

API_URL = "http://api.citybik.es" + "/v2"


class CityBikesEndpoint(Enum):
    GetAllNetworks = API_URL, "/networks"
    GetNetwork = API_URL, "/networks/{network_id}"

    def url(self, **kwargs):
        url_base, path = self.value

        return url_base + path.format(**kwargs)
