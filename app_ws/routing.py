from django.urls import re_path

from . import consumers

urlpatterns = [re_path("ws-test", consumers.TestConsumer.as_asgi())]
