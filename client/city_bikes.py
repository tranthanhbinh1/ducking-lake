import requests
from .endpoints import CityBikesEndpoint
from .schemas import NetworkDetailResponse, Networks
from typing import Type, TypeVar
from pydantic import BaseModel
from utils.logger import logger

T = TypeVar("T", bound=BaseModel)


class CityBikesClient:
    def __init__(self):
        pass

    def _make_request(self, endpoint: CityBikesEndpoint, model: Type[T], **kwargs):
        response = requests.get(endpoint.url(**kwargs))
        response.raise_for_status()
        resp_json = response.json()
        logger.info(resp_json)
        return model(**resp_json)

    def get_all_networks(self):
        return self._make_request(CityBikesEndpoint.GetAllNetworks, Networks)

    def get_network_by_id(self, network_id: str) -> NetworkDetailResponse:
        return self._make_request(
            CityBikesEndpoint.GetNetwork, NetworkDetailResponse, network_id=network_id
        )


# Quick test
if __name__ == "__main__":
    client = CityBikesClient()
    resp = client.get_network_by_id("velib")
