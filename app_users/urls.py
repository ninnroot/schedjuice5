from django.urls import path
from . import views

urlpatterns = [
    path('staffs/', views.StaffListView.as_view(), name='staff-list'),
    path('staffs/research', views.StaffResearchView.as_view(), name='staff-list'),
    path('staffs/<int:obj_id>', views.StaffDetailsView.as_view(), name='staff-details'),
]