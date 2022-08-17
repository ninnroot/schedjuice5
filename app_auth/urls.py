from django.urls import path
from app_auth import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("accounts", views.AccountListView.as_view(), name="account-list"),
    path("accounts/<int:pk>", views.AccountDetailsView.as_view(), name="account-detail"),
    path("accounts/search", views.AccountSearchView.as_view(), name="account-search"),
    
    path("login", views.LoginView.as_view()),
]
