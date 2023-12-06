from app.exception.subsrciber import SubscriberFoundException, ValidationError
from app.models import UserSubscriber as ModelUserSubscriber
from app.serializer.subsrciber import SubscriberSerializer
from app.repository.subsrciber import UserSubscriber
from rest_framework.views import exception_handler


class SubscriberUser:
    subscriber_repository = UserSubscriber()

    def subscribe(self, subscriber_serializer: SubscriberSerializer) -> None:

        if not subscriber_serializer.is_valid():
            raise ValidationError(subscriber_serializer.errors)

        subscriber = self.subscriber_repository.find_by_email(subscriber_serializer.get_email)

        if subscriber:
            raise SubscriberFoundException()

        ModelUserSubscriber(email=subscriber_serializer.get_email).save()
        



