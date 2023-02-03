from django.urls import path

from . import views

urlpatterns = [
    path(
        "availabilities/<str:model>/<int:obj_id>",
        views.AvailabilityView.as_view(),
        name="availability-view",
    )
]
