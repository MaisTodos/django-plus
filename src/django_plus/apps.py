from django.apps import AppConfig
from suit.apps import DjangoSuitConfig


class SuitConfig(DjangoSuitConfig):
    layout = "horizontal"



class UtilsConfig(AppConfig):
    name = "utils"

    def ready(self):
        import django_plus.signals  # noqa
