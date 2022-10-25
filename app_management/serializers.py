from rest_framework.serializers import ValidationError

from schedjuice5.serializers import BaseModelSerializer

from .models import *


# Base Validate Serailizer for checking cycular hierarcy.
class ValidateCyclicCTESerializer(BaseModelSerializer):
    def validate(self, attrs):
        if self.instance and "parent" in attrs and attrs["parent"] is not None:
            if attrs["parent"].id in [
                i.id for i in self.Meta.model.objects.get_nested(root_id=self.instance.id).all()
            ]:
                raise ValidationError(
                    {
                        "parent": f"Cyclic relationship. {self.Meta.model.__name__} {self.instance.name} cannot be a child of its own child."
                    }
                )
        return attrs
        

class GroupSerializer(ValidateCyclicCTESerializer):
    class Meta:
        model = Group
        fields = "__all__"

    expandable_fields = {
        "staffgroup_set": (
            "app_management.serializers.StaffGroupSerializer",
            {"many": True},
        ),
        "grouprole_set": (
            "app_management.serializers.GroupRoleSerializer",
            {"many": True},
        ),
    }


class DepartmentSerializer(ValidateCyclicCTESerializer):
    class Meta:
        model = Department
        fields = "__all__"

    expandable_fields = {
        "staffdepartment_set": (
            "app_management.serializers.StaffDepartmentSerializer",
            {"many": True},
        ),
    }


class JobSerializer(BaseModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

    expandable_fields = {
        "staffdepartment_set": (
            "app_management.serializers.StaffDepartmentSerializer",
            {"many": True},
        ),
        "staffcourse_set": (
            "app_management.serializers.StaffCourseSerializer",
            {"many": True},
        ),
        "staffevent_set": (
            "app_management.serializers.StaffEventSerializer",
            {"many": True},
        ),
    }


class RoleSerializer(BaseModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

    expandable_fields = {
        "staffrole_set": (
            "app_management.serializers.StaffRoleSerializer",
            {"many": True},
        ),
        "grouprole_set": (
            "app_management.serializers.GroupRoleSerializer",
            {"many": True},
        ),
        "rolepermission_set": (
            "app_management.serializers.RolePermissionSerializer",
            {"many": True},
        ),
    }


class PermissionSerializer(BaseModelSerializer):
    class Meta:
        model = Permission
        fields = "__all__"

    expandable_fields = {
        "rolepermission_set": (
            "app_management.serializers.RolePermissionSerializer",
            {"many": True},
        ),
    }


class StaffGroupSerializer(BaseModelSerializer):
    class Meta:
        model = StaffGroup
        fields = "__all__"

    expandable_fields = {
        "staff": ("app_users.serializers.StaffSerializer"),
        "group": ("app_management.serializers.GroupSerializer"),
    }


class StaffDepartmentSerializer(BaseModelSerializer):
    class Meta:
        model = StaffDepartment
        fields = "__all__"

    expandable_fields = {
        "staff": ("app_users.serializers.StaffSerializer"),
        "department": ("app_management.serializers.DepartmentSerializer"),
        "job": ("app_management.serializers.JobSerializer"),
    }


class StaffCourseSerializer(BaseModelSerializer):
    class Meta:
        model = StaffCourse
        fields = "__all__"

    expandable_fields = {
        "staff": ("app_users.serializers.StaffSerializer"),
        "job": ("app_management.serializers.JobSerializer"),
        "course": ("app_course.serializers.CourseSerializer"),
    }

    def validate(self, attrs):
        # check if the Events collide

        return super().validate(attrs)


class StaffEventSerializer(BaseModelSerializer):
    class Meta:
        model = StaffEvent
        fields = "__all__"

    expandable_fields = {
        "staff": ("app_users.serializers.StaffSerializer"),
        "job": ("app_management.serializers.JobSerializer"),
        "event": ("app_course.serializers.EventSerializer"),
    }

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

    expandable_fields = {
        "staff": ("app_users.serializers.StaffSerializer"),
        "role": ("app_users.serializers.RoleSerializer"),
    }


class GroupRoleSerializer(BaseModelSerializer):
    class Meta:
        model = GroupRole
        fields = "__all__"

    expandable_fields = {
        "group": ("app_users.serializers.GroupSerializer"),
        "role": ("app_users.serializers.RoleSerializer"),
    }


class RolePermissionSerializer(BaseModelSerializer):
    class Meta:
        model = RolePermission
        fields = "__all__"

    expandable_fields = {
        "permission": ("app_users.serializers.PermissionSerializer"),
        "role": ("app_users.serializers.RoleSerializer"),
    }
