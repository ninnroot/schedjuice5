from django.urls import path
from app_auth import views

urlpatterns = [
    path("", views.Test.as_view())
]