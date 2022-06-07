from suconnect_1.views import BaseListView
from app_finance.models import Record
from app_finance.serializers import RecordSerializer

class RecordView(BaseListView):

    name = "Record list view"
    description = "You can get the list of Record objects here"

    model = Record
    serializer = RecordSerializer




