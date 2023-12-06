from app.models import Subscriber


class UserSubscriberRepository():
    subscriber_model = Subscriber

    def find_by_email(self, email: str) -> Subscriber | None:
        return self.subscriber_model.objects.filter(email=email).first()
