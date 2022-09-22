from schedjuice5.serializers import BaseModelSerializer

from .models import *


class CategorySerializer(BaseModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class EventClassificationSerializer(BaseModelSerializer):
    class Meta:
        model = EventClassification
        fields = "__all__"


class CourseSerializer(BaseModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class EventSerializer(BaseModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"


class EventVenueSerializer(BaseModelSerializer):
    class Meta:
        model = EventVenue
        fields = "__all__"


class CalendarSerializer(BaseModelSerializer):
    class Meta:
        model = Calendar
        fields = "__all__"
