from rest_framework.views import APIView
from rest_framework.response import Response
from app.service.subsrciber import SubscriberUser


class Subscriber(APIView):
    def get(self, request):
        SubscriberUser().subscribe(request)

        return Response({
            "message": "Subscriber has been created successfully!",
            "details": "Operation has been completed with no errors"
        })