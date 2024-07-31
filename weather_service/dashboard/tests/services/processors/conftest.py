import pytest

from weather_service.dashboard.models.models import WeatherData
from weather_service.dashboard.services.processors.analyzer import (
    HumidityAnalyzer,
    TemperatureAnalyzer,
    WeatherConditionAnalyzer,
)


@pytest.fixture
def weather_data_list() -> list[WeatherData]:
    return [
        WeatherData(
            city_name="1",
            country_code="DE",
            temperature=1,
            humidity=2,
            condition="Rain",
        ),
        WeatherData(
            city_name="2",
            country_code="DE",
            temperature=1,
            humidity=6,
            condition="Cloud",
        ),
        WeatherData(
            city_name="3",
            country_code="DE",
            temperature=2,
            humidity=5,
            condition="Rain",
        ),
        WeatherData(
            city_name="4",
            country_code="DE",
            temperature=2,
            humidity=4,
            condition="Rain",
        ),
    ]


@pytest.fixture
def temperature_analyzer(weather_data_list) -> TemperatureAnalyzer:
    return TemperatureAnalyzer(weather_data_list)


@pytest.fixture
def humidity_analyzer(weather_data_list) -> HumidityAnalyzer:
    return HumidityAnalyzer(weather_data_list)


@pytest.fixture
def weather_condition_analyzer(weather_data_list) -> WeatherConditionAnalyzer:
    return WeatherConditionAnalyzer(weather_data_list)
