from django.apps import AppConfig
from suit.apps import DjangoSuitConfig
from rangefilter.apps import RangeFilterConfig


class SuitConfig(DjangoSuitConfig):
    layout = "horizontal"


class DateRangeConfig(RangeFilterConfig):
    pass


class DjangoPlusConfig(AppConfig):
    name = "django_plus"

    def ready(self):
        import django_plus.signals  # noqa
