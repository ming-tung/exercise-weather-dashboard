from dataclasses import dataclass
from typing import Optional


@dataclass
class Location:
    lat: float
    lon: float
    city_name: str
    country_code: str
    state_code: Optional[str] = None  # only for the US


@dataclass
class WeatherData:
    city_name: str
    country_code: str
    humidity: float
    temperature: float
    condition: str
    state_code: Optional[str] = None  # only for the US


@dataclass
class Insights:
    highest_temperature: float
    cities_with_highest_temperature: list[str]
    lowest_humidity: float
    cities_with_lowest_humidity: list[str]
    most_common_condition: str
