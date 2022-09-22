from django.urls import path
from rest_framework.schemas.generators import EndpointEnumerator

from app_docs import views

urlpatterns = [path("docs/", views.DocView.as_view())]
