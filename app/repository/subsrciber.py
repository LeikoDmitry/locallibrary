from app.models import UserSubscriber as ModelUserSubscriber


class UserSubscriber:
    _model_subscriber = ModelUserSubscriber()

    def find_by_email(self, email: str) -> ModelUserSubscriber | None:
        return self._model_subscriber.objects.get(email=email)
