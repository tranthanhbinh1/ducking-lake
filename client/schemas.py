from typing import Optional
from pydantic import BaseModel, ConfigDict
from pydantic_extra_types.country import CountryAlpha2


class Data(BaseModel):
    """
    Base class for all data models
    """

    model_config = ConfigDict(extra="allow")


class Location(BaseModel):
    latitude: float
    city: str
    longitude: float
    country: str


class Network(BaseModel):
    company: list[str]
    href: str
    location: Location
    name: str
    id: str


class Networks(BaseModel):
    networks: Optional[list[Network]]
