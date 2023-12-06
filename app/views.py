from rest_framework import status
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from app.serializer.subsrciber import SubscriberSerializer
from app.service.subscriber import SubscriberService


class Subscriber(APIView):
    service = SubscriberService()

    def post(self, request):
        serializer = SubscriberSerializer(data=JSONParser().parse(request))
        self.service.subscribe(serializer)

        return Response({
            "details": "Subscriber has been created successfully!",
            "status_code": status.HTTP_200_OK
        })