from django.urls import path
from . import views

urlpatterns = [
    path('countries/', views.CountryView.as_view(), name='countries'),
    path('careers/', views.CareerView.as_view(), name='carrers'),
]

