from django.urls import path

from . import views

urlpatterns = [
    path("assignments/", views.AssignmentListView.as_view(), name="assignment-list"),
    path("assignments/search", views.AssignmentSearchView.as_view(), name="assignment-search"),
    path(
        "assignments/<int:obj_id>",
        views.AssignmentDetailsView.as_view(),
        name="assignment-details",
    ),
    
    path("asgnt-attachments/", views.AttachmentListView.as_view(), name="attachment-list"),
    path("asgnt-attachments/search", views.AttachmentSearchView.as_view(), name="attachment-search"),
    path(
        "asgnt-attachments/<int:obj_id>",
        views.AttachmentDetailsView.as_view(),
        name="attachment-details",
    ),
    
    path("submissions/", views.SubmissionListView.as_view(), name="submissions-list"),
    path("submissions/search", views.SubmissionSearchView.as_view(), name="submissions-search"),
    path(
        "submissions/<int:obj_id>",
        views.SubmissionDetailsView.as_view(),
        name="attachment-details",
    ),
    
    path("sub-attachments/", views.SubmissionAttachmentListView.as_view(), name="sub-attachments-list"),
    path("sub-attachments/search", views.SubmissionAttachmentSearchView.as_view(), name="sub-attachments-search"),
    path(
        "sub-attachments/<int:obj_id>",
        views.SubmissionAttachmentDetailsView.as_view(),
        name="attachment-details",
    ),
    
    path("course-assignments/", views.CourseAssignmentListView.as_view(), name="course-assignments-list"),
    path("course-assignments/search", views.CourseAssignmentSearchView.as_view(), name="course-assignments-search"),
    path(
        "course-assignments/<int:obj_id>",
        views.CourseAssignmentDetailsView.as_view(),
        name="course-assignments-details",
    ),
]