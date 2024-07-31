from unittest.mock import patch

from weather_service.dashboard.models.models import Insights
from weather_service.dashboard.services.processors import parser
from weather_service.dashboard.services.processors.analyzer import (
    HumidityAnalyzer,
    TemperatureAnalyzer,
    WeatherConditionAnalyzer,
)
from weather_service.dashboard.services.weather_data_service import (
    get_insights,
    get_weather_data_list,
)


@patch.object(parser, "get_location")
@patch.object(parser, "get_current_weather_data")
def test_get_weather_data_list(mock_get_current_weather_data, mock_get_location):
    locations = ["Berlin, DE; London, UK"]

    weather_data_list = get_weather_data_list(locations)

    assert mock_get_location.call_count == len(locations)
    assert mock_get_current_weather_data.call_count == len(locations)
    assert len(locations) == len(weather_data_list)


@patch.object(TemperatureAnalyzer, "highest_temperature", return_valuee="1")
@patch.object(
    TemperatureAnalyzer, "cities_with_highest_temperature", return_valuee=["A"]
)
@patch.object(HumidityAnalyzer, "lowest_humidity", return_valuee="2")
@patch.object(HumidityAnalyzer, "cities_with_lowest_humidity", return_valuee=["B", "C"])
@patch.object(WeatherConditionAnalyzer, "most_common_condition", return_valuee="Rain")
def test_get_insights(
    mock_most_common_condition,
    mock_cities_with_lowest_humidity,
    mock_lowest_humidity,
    mock_cities_with_highest_temperature,
    mock_highest_temperature,
):
    insights = get_insights([])

    assert isinstance(insights, Insights)
    assert insights.highest_temperature == mock_highest_temperature
    assert (
        insights.cities_with_highest_temperature == mock_cities_with_highest_temperature
    )
    assert insights.lowest_humidity == mock_lowest_humidity
    assert insights.cities_with_lowest_humidity == mock_cities_with_lowest_humidity
    assert insights.most_common_condition == mock_most_common_condition
