from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response

from app.serializer.subsrciber import SubscriberSerializer
from app.service.subsrciber import SubscriberUser


class Subscriber(APIView):
    def post(self, request):
        serializer = SubscriberSerializer(data=JSONParser().parse(request))
        SubscriberUser().subscribe(serializer)

        return Response({
            "message": "Subscriber has been created successfully!",
            "details": "Operation has been completed with no errors"
        })