import os

import requests

from weather_service.dashboard.services.exceptions import APIException

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENWEATHER_API_URL_BASE = "https://api.openweathermap.org"
LOCATION_API = (
    f"{OPENWEATHER_API_URL_BASE}/geo/1.0/direct?appid={OPENWEATHER_API_KEY}&limit=1"
)
CURRENT_WEATHER_API = f"{OPENWEATHER_API_URL_BASE}/data/2.5/weather?appid={OPENWEATHER_API_KEY}&units=metric"


def get_location(location: str) -> dict:
    location_url = f"{LOCATION_API}&limit=1&q={location}"
    try:
        request = requests.get(location_url)
        if len(request.json()) < 1:
            raise APIException(f"No location found found for {location}.")
        return request.json()[0]
    except Exception as e:
        raise APIException(f"Failed to get location for {location}: {e}")


def get_current_weather_data(lat: float, lon: float) -> dict:
    current_weather_url = f"{CURRENT_WEATHER_API}&lat={lat}&lon={lon}"
    try:
        request = requests.get(current_weather_url)
        return request.json()
    except Exception as e:
        raise APIException(
            f"Failed to get current weather data for (lat, lon): ({lat}, {lon}): {e}"
        )
