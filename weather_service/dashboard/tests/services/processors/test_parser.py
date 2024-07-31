from unittest.mock import patch

from weather_service.dashboard.models.models import Location, WeatherData
from weather_service.dashboard.services.api_clients import openweather_api
from weather_service.dashboard.services.processors.parser import (
    get_current_weather_data,
    get_location,
)


@patch.object(
    openweather_api,
    "get_location",
    return_value={"lat": 123, "lon": 456, "name": "Berlin", "country": "DE"},
)
def test_get_location(mock_get_openweather_location):
    location = get_location("Berlin, DE")

    mock_get_openweather_location.assert_called_once_with("Berlin, DE")
    assert location == Location(lat=123, lon=456, city_name="Berlin", country_code="DE")


@patch.object(
    openweather_api,
    "get_current_weather_data",
    return_value={"main": {"temp": 10, "humidity": 20}, "weather": [{"main": "Rain"}]},
)
def test_get_current_weather_data(mock_get_current_weather_data):
    location = Location(lat=123, lon=456, city_name="Berlin", country_code="DE")

    weather_data = get_current_weather_data(location)

    mock_get_current_weather_data.assert_called_once_with(location.lat, location.lon)
    assert weather_data == WeatherData(
        city_name=location.city_name,
        country_code=location.country_code,
        temperature=10,
        humidity=20,
        condition="Rain",
    )
