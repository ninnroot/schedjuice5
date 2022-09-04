from app_auth.models import Account
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from app_auth.serializers import LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):

        invalidated_cred = LoginSerializer(data=request.data)

        if not invalidated_cred.is_valid():
            raise AuthenticationFailed({"data": invalidated_cred.errors})

        account = Account.objects.get(email=request.data["email"])
        if not account:

            raise AuthenticationFailed("No such account", code="user_not_found")
        if account.check_password(request.data["password"]):
            return (account, None)

        raise AuthenticationFailed("Invalid credentials")


def get_token(user):
    refresh = RefreshToken.for_user(user)
    data = {"refresh": str(refresh), "access": str(refresh.access_token)}

    return data

