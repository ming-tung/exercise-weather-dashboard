import pytest

from weather_service.dashboard.views import parse_locations_from_request


@pytest.mark.parametrize(
    "locations, expected_parsed_locations",
    (
        ("", [""]),
        ("Berlin, DE", ["Berlin, DE"]),
        ("Berlin, DE; London, UK", ["Berlin, DE", "London, UK"]),
        ("Berlin, DE; NYC, 12345, US", ["Berlin, DE", "NYC, 12345, US"]),
    ),
)
def test_parse_locations_from_request(locations, expected_parsed_locations):
    parsed_locations = parse_locations_from_request(locations)
    assert parsed_locations == expected_parsed_locations
