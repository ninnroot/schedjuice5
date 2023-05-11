from utilitas.serializers import BaseModelSerializer

from app_microsoft.flows import CreateTeamFlow

from .models import *


class CategorySerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Category
        fields = "__all__"

    expandable_fields = {
        "courses": ("app_course.serializers.CourseSerializer", {"many": True})
    }


class CourseSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Course
        fields = "__all__"
        extra_kwargs = {"channel_id": {"required": False}, "ms_id": {"required": False}}

    expandable_fields = {
        "category": ("app_course.serializers.CategorySerializer"),
        "events": ("app_course.serializers.EventSerializer", {"many": True}),
        "staffs_courses": (
            "app_management.serializers.StaffCourseSerializer",
            {"many": True},
        ),
        "students_courses": (
            "app_management.serializers.StudentCourseSerializer",
            {"many": True},
        ),
    }

    def create(self, validated_data):
        # start the team creation flow
        flow = CreateTeamFlow(validated_data["name"])
        x = flow.start()
        # populate with returned data
        validated_data["channel_id"] = x["channel_id"]
        validated_data["ms_id"] = x["group_id"]

        return super().create(validated_data)


class EventSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Event
        fields = "__all__"

    expandable_fields = {
        "course": ("app_course.serializers.CourseSerializer"),
        "classification": ("app_course.serializers.EventClassificationSerializer"),
        "events_venues": (
            "app_course.serializers.EventVenueSerializer",
            {"many": True},
        ),
        "staffs_events": (
            "app_management.serializers.StaffEventSerializer",
            {"many": True},
        ),
    }


class EventVenueSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = EventVenue
        fields = "__all__"

    expandable_fields = {
        "event": ("app_course.serializers.EventSerializer"),
        "venue": ("app_campus.serializers.VenueSerializer"),
    }


class CalendarSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Calendar
        fields = "__all__"

    expandable_fields = {}
