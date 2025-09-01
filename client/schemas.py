from typing import Optional, Any
from datetime import datetime
from pydantic import BaseModel, ConfigDict, field_validator
from pydantic_extra_types.country import CountryAlpha2
from utils.parsers import parse_timestamp


class Data(BaseModel):
    """
    Base class for all data models
    """

    model_config = ConfigDict(extra="allow")


class Location(BaseModel):
    latitude: float
    city: str
    longitude: float
    country: CountryAlpha2 | str


class Network(BaseModel):
    company: list[str]
    href: str
    location: Location
    name: str
    id: str


class Networks(BaseModel):
    networks: Optional[list[Network]]


class Station(BaseModel):
    id: str
    name: str
    latitude: float
    longitude: float
    timestamp: datetime
    free_bikes: int
    empty_slots: int
    extra: Optional[dict[str, Any]] = None

    @field_validator("timestamp", mode="before")
    @classmethod
    def validate_timestamp(cls, v):
        return parse_timestamp(v)


class Vehicle(BaseModel):
    id: str
    latitude: float
    longitude: float
    timestamp: datetime
    kind: str
    extra: Optional[dict[str, Any]] = None

    @field_validator("timestamp", mode="before")
    @classmethod
    def validate_timestamp(cls, v):
        return parse_timestamp(v)


class NetworkDetail(BaseModel):
    id: str
    name: str
    location: Location
    href: str
    company: list[str]
    stations: Optional[list[Station]] = None
    vehicles: Optional[list[Vehicle]] = None


class NetworkDetailResponse(BaseModel):
    network: NetworkDetail
