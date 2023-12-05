from django.db import models


class UserSubscriber(models.Model):
    email = models.EmailField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "User Subscriber"
