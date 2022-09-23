from django.urls import path

from . import views

urlpatterns = [
    path("countries/", views.CountryView.as_view(), name="countries"),
    path("careers/", views.CareerView.as_view(), name="carrers"),
    path("dial_codes/", views.DialCodeView.as_view(), name="dial_codes"),
    path("postal_codes/get/", views.PostalCodeView.as_view(), name="postal_codes"),
    path(
        "postal_codes/<str:postal_code>/get/",
        views.PostalCodeView.as_view(),
        name="postal_codes",
    ),
]
