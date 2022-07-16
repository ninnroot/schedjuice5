from django.urls import path
from app_auth import views

urlpatterns = [path("accounts", views.AccountListView.as_view())]
