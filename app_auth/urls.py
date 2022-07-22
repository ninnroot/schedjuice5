from django.urls import path
from app_auth import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("accounts", views.AccountListView.as_view()),
    path("login", views.LoginView.as_view()),
]
