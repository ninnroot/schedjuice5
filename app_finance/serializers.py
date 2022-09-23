from app_finance.models import Record
from schedjuice5.serializers import BaseModelSerializer


class RecordSerializer(BaseModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"
