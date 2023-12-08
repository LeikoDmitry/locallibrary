import json

from app.exception.subsrciber import SubscriberFoundError
from app.models import Subscriber
from app.serializer.subsrciber import SubscriberSerializer
from app.repository.subsrciber import UserSubscriberRepository


class SubscriberService:

    def __init__(self, repository: UserSubscriberRepository):
        self.subscriber_repository = repository

    def subscribe(self, subscriber_serializer: SubscriberSerializer) -> None:
        subscriber = self.subscriber_repository.find_by_email(email=subscriber_serializer.get_email)

        if subscriber:
            raise SubscriberFoundError()

        Subscriber(email=subscriber_serializer.get_email).save()