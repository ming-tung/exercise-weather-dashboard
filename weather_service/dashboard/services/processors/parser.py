from weather_service.dashboard.models.models import Location, WeatherData
from weather_service.dashboard.services.api_clients import openweather_api


def get_location(location: str) -> Location:
    data = openweather_api.get_location(location)
    # TODO state_code for US
    return Location(
        lat=data["lat"],
        lon=data["lon"],
        city_name=data["name"],
        country_code=data["country"],
    )


def get_current_weather_data(location: Location) -> WeatherData:
    data = openweather_api.get_current_weather_data(location.lat, location.lon)
    weather_data = {
        "city_name": location.city_name,
        "country_code": location.country_code,
        "temperature": data["main"]["temp"],
        "condition": data["weather"][0]["main"],
        "humidity": data["main"]["humidity"],
    }
    return WeatherData(**weather_data)
