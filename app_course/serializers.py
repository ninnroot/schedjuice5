from schedjuice5.serializers import BaseModelSerializer

from .models import *


class CategorySerializer(BaseModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    expandable_fields = {
        "course_set": ("app_course.serializers.CourseSerializer", {"many": True})
    }


class EventClassificationSerializer(BaseModelSerializer):
    class Meta:
        model = EventClassification
        fields = "__all__"

    expandable_fields = {
        
    }


class CourseSerializer(BaseModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"

    expandable_fields = {
        "category": ("app_course.serializers.CategorySerializer"),
        "event_set": ("app_course.serializers.EventSerializer", {"many": True}),
        "staffcourse_set": ("app_management.serializers.StaffCourseSerializer", {"many": True}),
    }


class EventSerializer(BaseModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    expandable_fields = {
        "course": ("app_course.serializers.CourseSerializer"),
        "classification": ("app_course.serializers.EventClassificationSerializer"),
        "eventvenue_set": ("app_course.serializers.EventVenueSerializer", {"many": True}),
        "staffevent_set": ("app_management.serializers.StaffEventSerializer", {"many": True}),
    }


class EventVenueSerializer(BaseModelSerializer):
    class Meta:
        model = EventVenue
        fields = "__all__"

    expandable_fields = {
        "event": ("app_course.serializers.EventSerializer"),
        "venue": ("app_campus.serializers.VenueSerializer")
    }


class CalendarSerializer(BaseModelSerializer):
    class Meta:
        model = Calendar
        fields = "__all__"

    expandable_fields = {
        
    }