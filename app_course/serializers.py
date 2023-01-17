from schedjuice5.serializers import BaseModelSerializer

from .models import *


class CategorySerializer(BaseModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

    expandable_fields = {
        "courses": ("app_course.serializers.CourseSerializer", {"many": True})
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
        "events": ("app_course.serializers.EventSerializer", {"many": True}),
        "staffs_courses": ("app_management.serializers.StaffCourseSerializer", {"many": True}),
        "students_courses": ("app_management.serializers.StudentCourseSerializer", {"many": True}),
    }


class EventSerializer(BaseModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    expandable_fields = {
        "course": ("app_course.serializers.CourseSerializer"),
        "classification": ("app_course.serializers.EventClassificationSerializer"),
        "events_venues": ("app_course.serializers.EventVenueSerializer", {"many": True}),
        "staffs_events": ("app_management.serializers.StaffEventSerializer", {"many": True}),
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