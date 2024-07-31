class WeatherServiceException(Exception):
    pass


class APIException(WeatherServiceException):
    pass


class ValidationError(Exception):
    pass
