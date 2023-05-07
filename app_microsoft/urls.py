from django.urls import path

from . import views

urlpatterns = [
    path(
        "microsoft/test",
        views.TestView.as_view(),
        name="ms-test-view",
    )
]
