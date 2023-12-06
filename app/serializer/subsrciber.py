from rest_framework import serializers

from app.exception.subsrciber import ValidationError
from app.models import UserSubscriber


class SubscriberSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=100)

    def validate_email(self, value):
        if UserSubscriber.objects.filter(email=value).exists():
            raise ValidationError("A user with this email already exists!")

        return value

    @property
    def get_email(self):
        return self.data.get('email')
