from django.urls import path, include
from . import views

urlpatterns = [
    path("venue-classifications", views.VenueClassificationListView.as_view(), name="venue-classification-list"),
    path("venue-classifications/<int:pk>", views.VenueClassificationDetailsView.as_view(), name="venue-classification-detail"),
    path("venue-classifications/search", views.VenueClassificationSearchView.as_view(), name="venue-classification-search"),

    path("campuses", views.CampusListView.as_view(), name="campus-list"),
    path("campuses/<int:pk>", views.CampusDetailsView.as_view(), name="campus-detail"),
    path("campuses/search", views.CampusSearchView.as_view(), name="campus-search"),

    path("venues", views.VenueListView.as_view(), name="venue-list"),
    path("venues/<int:pk>", views.VenueDetailsView.as_view(), name="venue-detail"),
    path("venues/search", views.VenueSearchView.as_view(), name="venue-search"),
]