from dependency_injector import containers, providers
from django.conf import settings

from app.service.subscriber import SubscriberService
from app.repository.subsrciber import UserSubscriberRepository


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    user_repository = providers.Factory(
        UserSubscriberRepository
    )

    service_subscriber = providers.Factory(
        SubscriberService,
        repository=user_repository
    )


container = Container()
container.config.from_dict(settings.__dict__)