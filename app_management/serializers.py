from rest_framework.serializers import ValidationError

from schedjuice5.serializers import BaseModelSerializer
from .models import *


class GroupSerializer(BaseModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class DepartmentSerializer(BaseModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class JobSerializer(BaseModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"


class RoleSerializer(BaseModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"


class PermissionSerializer(BaseModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"


class StaffGroupSerializer(BaseModelSerializer):
    class Meta:
        model = StaffGroup
        fields = "__all__"


class StaffDepartmentSerializer(BaseModelSerializer):
    class Meta:
        model = StaffDepartment
        fields = "__all__"


class StaffCourseSerializer(BaseModelSerializer):
    class Meta:
        model = StaffCourse
        fields = "__all__"

    def validate(self, attrs):
        # check if the Events collide

        return super().validate(attrs)


class StaffEventSerializer(BaseModelSerializer):
    class Meta:
        model = StaffEvent
        fields = "__all__"

    def validate(self, attrs):
        # TODO: check event status and filter further
        same_day_events = StaffEvent.objects.filter(
            date=attrs.date, staff=attrs.staff
        ).all()
        for i in same_day_events:
            if not (
                (attrs.time_from >= i.time_to and attrs.time_to >= i.time_to)
                or (attrs.time_from <= i.time_from and attrs.time_to <= i.time_to)
            ):
                raise ValidationError(f"Event colliding with event ({i}).")

        return super().validate(attrs)


class StaffRoleSerializer(BaseModelSerializer):
    class Meta:
        model = StaffRole
        fields = "__all__"


class GroupRoleSerializer(BaseModelSerializer):
    class Meta:
        model = GroupRole
        fields = "__all__"


class RolePermissionSerializer(BaseModelSerializer):
    class Meta:
        model = RolePermission
        fields = "__all__"
