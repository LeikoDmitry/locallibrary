from app.models import UserSubscriber as ModelSubscriber


class UserSubscriber:
    def __int__(self):
        self._model_subscriber = ModelSubscriber

    def find_by_id(self, id: int) -> ModelSubscriber | None:
        return self._model_subscriber.objects.get(id=id)
