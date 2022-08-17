from schedjuice5.serializers import BaseModelSerializer
from .models import *

class VenueClassificationSerializer(BaseModelSerializer):
    class Meta:
        model = VenueClassification
        fields = "__all__"


class CampusSerializer(BaseModelSerializer):
    class Meta:
        model = Campus
        fields = "__all__"


class VenueSerializer(BaseModelSerializer):
    class Meta:
        model = Venue
        fields = "__all__"