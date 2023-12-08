from django.urls import path

from app.repository.subsrciber import UserSubscriberRepository
from app.service.subscriber import SubscriberService
from app.views import Subscriber

subscribe_service = SubscriberService(UserSubscriberRepository())

urlpatterns = [
    path("subscribe", Subscriber.as_view(subscribe_service=subscribe_service), name="api_subscribe"),
]
