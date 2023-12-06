from rest_framework import status
from rest_framework.exceptions import ValidationError as BaseValidationError


class SubscriberFoundException(Exception):
    def __init__(self, message="Subscriber already exist!"):
        super().__init__(message)


class ValidationError(BaseValidationError):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY

    def __int__(self, detail):
        super().__init__(detail=detail)