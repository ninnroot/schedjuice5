from utilitas.serializers import BaseModelSerializer

from .models import *


class AddressSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Address
        fields = "__all__"

    expandable_fields = {"account": ("app_auth.serializers.AccountSerializer",)}


class PhoneNumberSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = PhoneNumber
        fields = "__all__"

    expandable_fields = {"account": ("app_auth.serializers.AccountSerializer",)}


class BankAccountSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = BankAccount
        fields = "__all__"

    expandable_fields = {"account": ("app_auth.serializers.AccountSerializer",)}


class StaffSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Staff
        fields = "__all__"

    expandable_fields = {
        "account": ("app_auth.serializers.AccountSerializer"),
        "staffs_groups": (
            "app_management.serializers.StaffGroupSerializer",
            {"many": True},
        ),
        "staffs_depts": (
            "app_management.serializers.StaffDepartmentSerializer",
            {"many": True},
        ),
        "staffs_courses": (
            "app_management.serializers.StaffCourseSerializer",
            {"many": True},
        ),
        "staffs_events": (
            "app_management.serializers.StaffEventSerializer",
            {"many": True},
        ),
        "staffs_roles": (
            "app_management.serializers.StaffRoleSerializer",
            {"many": True},
        ),
    }


class GuardianSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Guardian
        fields = "__all__"

    expandable_fields = {"account": ("app_auth.serializers.AccountSerializer")}


class StudentSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Student
        fields = "__all__"

    expandable_fields = {
        "account": ("app_auth.serializers.AccountSerializer"),
        "staffs_courses": (
            "app_management.serializers.StaffCourseSerializer",
            {"many": True},
        ),
    }
