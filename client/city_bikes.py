import requests
from .endpoints import CityBikesEndpoint
from .schemas import Networks
from typing import Type, TypeVar
from pydantic import BaseModel

T = TypeVar("T", bound=BaseModel)


class CityBikesClient:
    def __init__(self):
        pass

    def _make_request(self, endpoint: CityBikesEndpoint, model: Type[T], **kwargs):
        response = requests.get(endpoint.url(**kwargs))
        response.raise_for_status()
        return model(**response.json())

    def get_all_networks(self):
        return self._make_request(CityBikesEndpoint.GetAllNetworks, Networks)


# Quick test
if __name__ == "__main__":
    client = CityBikesClient()
    resp = client.get_all_networks()

    print(len(resp.networks))
