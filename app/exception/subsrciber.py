from rest_framework import status
from rest_framework.exceptions import APIException


class SubscriberFoundError(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = "Subscriber already exist!"
    default_code = 'not_found'


class ValidationError(APIException):
    status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
    default_detail = 'Validation Error'
    default_code = 'invalid'
