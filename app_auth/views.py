from schedjuice5.views import BaseListView
from app_auth.models import Account
from app_auth.serializers import AccountSerializer


class AccountListView(BaseListView):
    name = "Account list view"
    model = Account
    serializer = AccountSerializer
