from schedjuice5.serializers import BaseModelSerializer

from .models import *


class VenueClassificationSerializer(BaseModelSerializer):
    class Meta:
        model = VenueClassification
        fields = "__all__"

    expandable_fields = {
        "venues": ("app_campus.serializers.VenueSerializer", {"many": True})
    }


class CampusSerializer(BaseModelSerializer):
    class Meta:
        model = Campus
        fields = "__all__"

    expandable_fields = {
        "venues": ("app_campus.serializers.VenueSerializer", {"many": True})
    }


class VenueSerializer(BaseModelSerializer):
    class Meta:
        model = Venue
        fields = "__all__"

    expandable_fields = {
        "campus": ("app_campus.serializers.CampusSerializer"),
        "classification": ("app_campus.serializers.VenueClassificationSerializer"),
        "events_venues": ("app_course.serializers.EventVenueSerializer", {"many": True})
    }
