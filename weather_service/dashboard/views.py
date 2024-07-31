from django.shortcuts import render
from django.views.decorators.http import require_GET

from django.http import HttpRequest, HttpResponse

from weather_service.dashboard.services import weather_data_service
from weather_service.dashboard.services.exceptions import (
    ValidationError,
    WeatherServiceException,
)


def parse_locations_from_request(locations: str) -> list[str]:
    try:
        locations = locations.split(";")
        return [location.strip(" ") for location in locations]
    except Exception as e:
        raise ValidationError(
            f"location {locations} input is not valid. Please see an example: Berlin, DE; London, UK"
        )


@require_GET
def dashboard(request: HttpRequest) -> HttpResponse:
    locations = parse_locations_from_request(request.GET.get("locations", ""))

    weather_data_list, insights, notification = [], [], ""
    try:
        weather_data_list = weather_data_service.get_weather_data_list(locations)
        insights = weather_data_service.get_insights(weather_data_list)
    except WeatherServiceException as err:
        notification = f"Something went wrong: {err}"
    except ValidationError as err:
        notification = f"{err}"

    return render(
        request,
        "index.html",
        {
            "locations": locations,
            "insights": insights,
            "weather_data_list": weather_data_list,
            "notification": notification,
        },
    )
