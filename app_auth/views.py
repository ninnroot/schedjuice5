from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.encoding import DjangoUnicodeDecodeError, smart_bytes, smart_str
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework import exceptions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import Request
from rest_framework_simplejwt.views import TokenObtainPairView
from utilitas.views import BaseDetailsView, BaseListView, BaseSearchView, BaseView

from app_auth.authentication import CustomAuthentication, get_token
from app_auth.models import Account, TempEmail
from app_auth.serializers import (
    AccountSerializer,
    LoginSerializer,
    MSLoginSerializer,
    RequestUpdateEmailSerializer,
)


# ------------ Account Section ------------
class AccountListView(BaseListView):
    name = "Account list view"
    model = Account
    serializer = AccountSerializer


class AccountDetailsView(BaseDetailsView):
    name = "Account details view"
    model = Account
    serializer = AccountSerializer


class AccountSearchView(BaseSearchView):
    name = "Account search view"
    model = Account
    serializer = AccountSerializer


class LoginView(TokenObtainPairView):
    name = "The login endpoint"
    serializer_class = LoginSerializer


class MSLoginView(TokenObtainPairView):
    name = "the new login method"
    serializer_class = MSLoginSerializer
