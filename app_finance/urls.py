from django.urls import path, include
from app_finance import views


urlpatterns = [
    path("/records", views.RecordView.as_view())
]
