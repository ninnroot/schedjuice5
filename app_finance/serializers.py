from schedjuice5.serializers import BaseModelSerializer
from app_finance.models import Record


class RecordSerializer(BaseModelSerializer):
    class Meta:
        model = Record
