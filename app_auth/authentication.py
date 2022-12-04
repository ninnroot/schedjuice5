from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from app_auth.models import Account
from app_auth.serializers import LoginSerializer


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):

        invalidated_cred = LoginSerializer(data=request.data)

        if not invalidated_cred.is_valid():
            raise AuthenticationFailed({"data": invalidated_cred.errors})

        account = Account.objects.filter(email=request.data["email"]).first()
        if not account:
            raise AuthenticationFailed("No such account", code="user_not_found")
        
        if account.check_password(request.data["password"]):
            return (account, get_token(account))

        raise AuthenticationFailed("Invalid credentials")
    

def get_token(user):
    refresh = RefreshToken.for_user(user)
    data = {"access": str(refresh.access_token)}

    return data
