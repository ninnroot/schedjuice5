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
    RequestUpdateEmailSerializer,
)
from app_microsoft.mail import send_mail
from app_users.serializers import GuardianSerializer, StaffSerializer, StudentSerializer


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


class RequestUpdateEmailView(BaseView):
    name = "Update email endpoint"
    serializer = RequestUpdateEmailSerializer
    # permission_classes = [IsAuthenticated]

    def post(self, request: Request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # user = request.user.account
        user = Account.objects.get(pk=1)  # this is for testing user

        # temporary storing for user's new email
        TempEmail.objects.create(account=user, email=serializer.data.get("email"))

        # prepare for activate_url
        uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
        token = default_token_generator.make_token(user)
        current_site = get_current_site(request).domain
        activate_url = f"http://{current_site}{reverse('verify-email', kwargs={'uidb64': str(uidb64), 'token': str(token), 'view': 'update-email'})}"
        send_mail(
            "Email Verification",
            activate_url,
            [serializer.data.get("email")],
        )

        return self.send_response(
            False,
            "success",
            {"details": "Verification email has sent!"},
            status=status.HTTP_200_OK,
        )


class EmailVerificationView(BaseView):
    def get(self, request, uidb64, token, view):
        try:
            id = urlsafe_base64_decode(uidb64)
            user = Account.objects.get(pk=id)

            # this is the action url, for further process after email validation
            current_site = get_current_site(request).domain
            action_url = f"http://{current_site}{reverse(view, kwargs={'uidb64': str(uidb64), 'token': str(token)})}"

            # if token is invalid, return error
            if not default_token_generator.check_token(user, token):
                return self.send_response(
                    True,
                    "bad_request",
                    {"details": "Token is invalid or expired"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # if token is valid, set is_active = True
            if not user.is_active:
                user.is_active = True
                user.save()

            return self.send_response(
                False,
                "success",
                {"details": "Email successfully confirmed", "action_url": action_url},
                status=status.HTTP_200_OK,
            )

        except Account.DoesNotExist:
            raise exceptions.AuthenticationFailed("This user doesn't exist")

        except DjangoUnicodeDecodeError:
            return self.send_response(
                True,
                "bad_request",
                {"details": "Token is invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class UpdateEmailView(BaseView):
    def get(self, request, uidb64, token):
        try:
            id = urlsafe_base64_decode(uidb64)
            user = Account.objects.get(pk=id)
            print(user)
            email = TempEmail.objects.get(account=user).email
            if not default_token_generator.check_token(user, token):
                return self.send_response(
                    True,
                    "bad_request",
                    {"details": "Token is invalid or expired"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.email = email
            user.save()

            # deleting temp-email after updating user's email
            TempEmail.objects.get(account=user).delete()

            return self.send_response(
                False,
                "success",
                {"details": "Email successfully updated"},
                status=status.HTTP_200_OK,
            )

        except Account.DoesNotExist:
            raise exceptions.AuthenticationFailed("This user doesn't exist")

        except DjangoUnicodeDecodeError:
            return self.send_response(
                True,
                "bad_request",
                {"details": "Token is invalid"},
                status=status.HTTP_400_BAD_REQUEST,
            )
