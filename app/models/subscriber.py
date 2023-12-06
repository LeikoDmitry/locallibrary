from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(max_length=255, null=False, unique=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Subscriber"
