from rest_framework import serializers
from app.models import Subscriber


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = ["email"]

    @property
    def get_email(self):
        return self.data.get('email')
