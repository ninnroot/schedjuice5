from django.urls import path, include
from app_finance import views

urlpatterns = [
    path("records", views.RecordListView.as_view(), name="record-list"),
    path("records/<int:pk>", views.RecordDetailsView.as_view(), name="record-detail"),
    path("records/search", views.RecordSearchView.as_view(), name="record-search"),
]
