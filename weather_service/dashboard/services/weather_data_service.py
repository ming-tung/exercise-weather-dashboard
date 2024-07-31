from weather_service.dashboard.models.models import Insights, WeatherData
from weather_service.dashboard.services.processors.analyzer import (
    HumidityAnalyzer,
    TemperatureAnalyzer,
    WeatherConditionAnalyzer,
)
from weather_service.dashboard.services.processors import parser


def get_weather_data_list(locations: list) -> list[WeatherData]:
    weather_data_list = []
    for location in locations:
        _location = parser.get_location(location)
        weather_data = parser.get_current_weather_data(_location)
        weather_data_list.append(weather_data)
    return weather_data_list


def get_insights(weather_data_list: list[WeatherData]) -> Insights:
    temperature_analyzer = TemperatureAnalyzer(weather_data_list)
    humidity_analyzer = HumidityAnalyzer(weather_data_list)
    weather_condition_analyzer = WeatherConditionAnalyzer(weather_data_list)

    insights = {
        "highest_temperature": temperature_analyzer.highest_temperature,
        "cities_with_highest_temperature": temperature_analyzer.cities_with_highest_temperature,
        "lowest_humidity": humidity_analyzer.lowest_humidity,
        "cities_with_lowest_humidity": humidity_analyzer.cities_with_lowest_humidity,
        "most_common_condition": weather_condition_analyzer.most_common_condition,
    }
    return Insights(**insights)
