# exercise-weather-dashboard

## System prerequisite and setup
- docker, docker-compose installed
- OpenWeather API Key in environment var: `OPENWEATHER_API_KEY`
- Put env var in the `dev.env` file


## Run service
```sh
docker-compose up

# or 
docker-compose build weather-service
docker-compose up
```

Service will be available http://localhost:8000/

## Fetch weather data
Fetch weather data via api_clients from external services, e.g.
- from OpenWeather API, see `api_clients/openweather.py` (required api key to be setup first)


## Parse and Analyze weather data
- Parse data from external service to internal data schema. See `processors/parser.py`
- Generate insights based on the data schema. See `processors/analyzer.py`

## Display weather data insight
- See in http://localhost:8000/

## Weather data model
- temperature
- humidity
- weather condition
- city name
- state code (optional, only for the US)
- country code


# Test
Run test using pytest: 
```sh
docker-compose -f docker-compose-test.yml build weather-service
docker-compose -f docker-compose-test.yml run weather-service
```

##  Shutdown all the services
```sh
docker-compose down --remove-orphans 
```


# Some of the TODOs
- Integration tests, e.g. test the `dashboard` function in `views.py` without calling external service.
- Test api clients. For example: use json files store locally in some fixtures to test the api clients.
- Tests for unhappy path, e.g. check if exceptions are raised properly.
- Possibly refactor to support async and Single page frontend
- Improve data analysis
- ...
