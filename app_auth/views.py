from schedjuice5.views import BaseListView, BaseView
from app_auth.models import Account
from app_auth.serializers import AccountSerializer, LoginSerializer
from rest_framework.views import Request, status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


class AccountListView(BaseListView):
    name = "Account list view"
    model = Account
    serializer = AccountSerializer


class LoginView(BaseView):
    name = "The login endpoint"
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request: Request):
        unauth_credentials = LoginSerializer(data=request.data)
        if unauth_credentials.is_valid():
            print(request.user)
            # token_pair = RefreshToken.for_user()
            print("ok")
            return self.send_response(False, "haha", {})

        return self.send_response(
            True,
            "bad_request",
            unauth_credentials.errors,
            status=status.HTTP_400_BAD_REQUEST,
        )
