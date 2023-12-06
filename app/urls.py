from django.urls import path
from app.views import Subscriber

urlpatterns = [
    path("subscribe", Subscriber.as_view(), name="api_subscribe"),
]