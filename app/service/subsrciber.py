from app.repository.subsrciber import UserSubscriber
from app.exception.subsrciber import SubscriberFoundException
from app.models import UserSubscriber as ModelUserSubscriber


class SubscriberUser:

    def __int__(self):
        self.subscriber_repository = UserSubscriber()

    def subscribe(self, subscriber_request) -> None:
        subscriber = self.subscriber_repository.find_by_email(subscriber_request.email)

        if subscriber:
            raise SubscriberFoundException()

        ModelUserSubscriber(email=subscriber_request.email).save()
        



