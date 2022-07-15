from app_docs import views
from django.urls import path
from rest_framework.schemas.generators import EndpointEnumerator

urlpatterns = [path("docs/", views.DocView.as_view())]
