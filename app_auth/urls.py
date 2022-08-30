from django.urls import path
from app_auth import views
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path("accounts", views.AccountListView.as_view(), name="account-list"),
    path("accounts/<int:obj_id>", views.AccountDetailsView.as_view(), name="account-detail"),
    path("accounts/search", views.AccountSearchView.as_view(), name="account-search"),
    
    path("login", views.LoginView.as_view()),

    path("email/request", views.RequestUpdateEmailView.as_view(), name='request-update'),
    path("email/verify/<uidb64>/<token>/<view>", views.EmailVerificationView.as_view(), name="verify-email"),
    path("email/update/<uidb64>/<token>", views.UpdateEmailView.as_view(), name="update-email")
]
