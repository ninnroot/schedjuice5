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
    
    path(
        "announcement-attachments/", views.AttachmentListView.as_view(), name="announcement-attachment-list"
    ),
    path(
        "announcement-attachments/<int:obj_id>",
        views.AttachmentDetailsView.as_view(),
        name="announcement-attachments-details",
    ),
    path(
        "announcement-attachments/search",
        views.AttachmentSearchView.as_view(),
        name="announcement-attachment-search",
    ),
]
