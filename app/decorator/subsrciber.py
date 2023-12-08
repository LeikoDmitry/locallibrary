import functools

from rest_framework.parsers import JSONParser

from app.exception.subsrciber import ValidationError
from app.serializer.subsrciber import SubscriberSerializer


class SubscriberRequest:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __get__(self, obj, object_type):
        """Support instance methods."""
        return functools.partial(self.__call__, obj)

    def __call__(self, obj, request):
        serializer = SubscriberSerializer(data=JSONParser().parse(request))

        if not serializer.is_valid():
            raise ValidationError({"details":  serializer.errors})

        return self.func(obj, request, serializer)