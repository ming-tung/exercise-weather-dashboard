class TestTemperatureAnalyzer:
    def test_highest_temperature(self, temperature_analyzer):
        assert 2 == temperature_analyzer.highest_temperature

    def test_cities_with_highest_temperature(self, temperature_analyzer):
        assert ["3", "4"] == temperature_analyzer.cities_with_highest_temperature


class TestHumidityAnalyzer:

    def test_lowest_humidity(self, humidity_analyzer):
        assert 2 == humidity_analyzer.lowest_humidity

    def test_cities_with_lowest_humidity(self, humidity_analyzer):
        assert ["1"] == humidity_analyzer.cities_with_lowest_humidity


class TestConditionAnalyzer:
    def test_most_common_conditions(self, weather_condition_analyzer):
        assert "Rain" == weather_condition_analyzer.most_common_condition
