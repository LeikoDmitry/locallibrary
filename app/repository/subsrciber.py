from app.models import UserSubscriber as ModelUserSubscriber


class UserSubscriber:
    model_subscriber = ModelUserSubscriber

    def find_by_email(self, email: str) -> ModelUserSubscriber | None:
        return self.model_subscriber.objects.filter(email=email).first()
