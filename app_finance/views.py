from suconnect_1.views import BaseListView
from app_finance.models import Record
from app_finance.serializers import RecordSerializer

class RecordView(BaseListView):

    model = Record
    serializer = RecordSerializer




