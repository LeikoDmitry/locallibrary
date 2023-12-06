import json

from app.exception.subsrciber import SubscriberFoundError, ValidationError
from app.models import Subscriber
from app.serializer.subsrciber import SubscriberSerializer
from app.repository.subsrciber import UserSubscriberRepository


class SubscriberService:
    subscriber_repository = UserSubscriberRepository()

    def subscribe(self, subscriber_serializer: SubscriberSerializer) -> None:

        if not subscriber_serializer.is_valid():
            raise ValidationError({"details":  subscriber_serializer.errors})

        subscriber = self.subscriber_repository.find_by_email(email=subscriber_serializer.get_email)

        if subscriber:
            raise SubscriberFoundError()

        Subscriber(email=subscriber_serializer.get_email).save()