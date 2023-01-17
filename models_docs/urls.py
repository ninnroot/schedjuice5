from django.urls import include, path

from . import views

urlpatterns = [
    path("models", views.home, name="models-docs"),
    path('models-json', views.ModelsDocsView.as_view(), name="models-json")
]
