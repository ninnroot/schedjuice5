from utilitas.views import BaseDetailsView, BaseListView, BaseSearchView

from app_finance.models import Record
from app_finance.serializers import RecordSerializer

#
# # ------------ Record Section ------------
# class RecordListView(BaseListView):
#     name = "Record list view"
#     model = Record
#     serializer = RecordSerializer
#
#
# class RecordDetailsView(BaseDetailsView):
#     name = "Record details view"
#     model = Record
#     serializer = RecordSerializer
#
#
# class RecordSearchView(BaseSearchView):
#     name = "Record search view"
#     model = Record
#     serializer = RecordSerializer
