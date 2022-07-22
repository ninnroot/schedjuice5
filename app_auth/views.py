from schedjuice5.views import BaseListView, BaseView
from app_auth.models import Account
from app_auth.serializers import AccountSerializer
from rest_framework.views import Request, status
from app_auth.authentication import CustomAuthentication
from app_auth.authentication import get_token


class AccountListView(BaseListView):
    name = "Account list view"
    model = Account
    serializer = AccountSerializer


class LoginView(BaseView):
    name = "The login endpoint"
    authentication_classes = [CustomAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request: Request):
        if request.user.is_authenticated:
            data = get_token(request.user)

            return self.send_response(False, "success", data, status=status.HTTP_200_OK)
