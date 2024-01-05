from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "app"

    def ready(self):
        from publisher.containers import Container
        container = Container()
        container.wire(modules=[".views"])

