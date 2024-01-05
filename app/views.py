from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from app.decorator.subsrciber import SubscriberRequest
from app.serializer.subsrciber import SubscriberSerializer
from dependency_injector.wiring import inject, Provide
from publisher.containers import Container
from app.service.subscriber import SubscriberService


class Subscriber(APIView):
    subscribe_service = None

    @inject
    def __init__(self, subscribe_service: SubscriberService = Provide[Container.service_subscriber], **kwargs):
        super().__init__(**kwargs)
        self.subscribe_service = subscribe_service

    @SubscriberRequest
    def post(self, request, serializer: SubscriberSerializer):
        self.subscribe_service.subscribe(serializer)

        return Response({
            "details": "Subscriber has been created successfully!",
            "status_code": status.HTTP_200_OK
        })
