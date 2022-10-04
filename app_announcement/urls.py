from django.urls import path

from app_announcement import views

urlpatterns = [
    path(
        "announcements/", views.AnnouncementListView.as_view(), name="announcement-list"
    ),
    path(
        "announcements/<int:obj_id>",
        views.AnnouncementDetailsView.as_view(),
        name="announcement-details",
    ),
    path(
        "announcements/search",
        views.AnnouncementSearchView.as_view(),
        name="announcement-search",
    ),
]
