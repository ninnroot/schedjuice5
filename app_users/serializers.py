from schedjuice5.serializers import BaseModelSerializer
from .models import Staff

class StaffSerializer(BaseModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"
    
        