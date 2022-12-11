from django.urls import include, path

from . import views

urlpatterns = [
    path("models", views.home, name="models-docs"),
]
