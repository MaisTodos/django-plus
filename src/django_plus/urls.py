
from django.views.generic import View
from django.http import HttpResponse
from django.urls import path


class PingView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("pong")


urlpatterns = [
    path(r"ping", PingView.as_view()),
]