from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    layout = "horizontal"


class DjangoPlusConfig(AppConfig):
    name = "django_plus"

    def ready(self):
        import django_plus.signals  # noqa
