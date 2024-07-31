from functools import cached_property

import pandas as pd

from weather_service.dashboard.models.models import WeatherData


class BaseAnalyzer:
    def __init__(self, weather_data_list: list[WeatherData]):
        self.weather_data_list = weather_data_list
        self.weather_data_list_df = pd.DataFrame(weather_data_list)


class TemperatureAnalyzer(BaseAnalyzer):
    KEY = "temperature"

    @cached_property
    def _data_sort_by_temperature_desc(self) -> pd.DataFrame:
        return self.weather_data_list_df.sort_values(self.KEY, ascending=False)

    @cached_property
    def highest_temperature(self) -> float:
        return float(self._data_sort_by_temperature_desc[self.KEY].iloc[0])

    @cached_property
    def cities_with_highest_temperature(self) -> list[str]:
        num_of_cities = int(
            self._data_sort_by_temperature_desc.groupby(self.KEY)["city_name"].count()[
                self.highest_temperature
            ]
        )
        return list(self._data_sort_by_temperature_desc["city_name"][:num_of_cities])


class HumidityAnalyzer(BaseAnalyzer):
    KEY = "humidity"

    @cached_property
    def _data_sort_by_humidity_asc(self) -> pd.DataFrame:
        return self.weather_data_list_df.sort_values(self.KEY)

    @cached_property
    def lowest_humidity(self) -> float:
        return float(self._data_sort_by_humidity_asc[self.KEY].iloc[0])

    @cached_property
    def cities_with_lowest_humidity(self) -> list[str]:
        num_of_cities = int(
            self._data_sort_by_humidity_asc.groupby(self.KEY)["city_name"].count()[
                self.lowest_humidity
            ]
        )
        return list(self._data_sort_by_humidity_asc["city_name"][:num_of_cities])


class WeatherConditionAnalyzer(BaseAnalyzer):
    @cached_property
    def most_common_condition(self) -> str:
        # Only support to return one most common condition at the moment.
        #  if there are multiple conditions having the same count. it would
        #  only return the first condition.
        return self.weather_data_list_df.condition.mode()[0]
