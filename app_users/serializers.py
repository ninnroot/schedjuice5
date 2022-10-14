from schedjuice5.serializers import BaseModelSerializer

from .models import *


class AddressSerializer(BaseModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    expandable_fields = {"account": ("app_auth.serializers.AccountSerializer",)}


class PhoneNumberSerializer(BaseModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = "__all__"

    expandable_fields = {"account": ("app_auth.serializers.AccountSerializer",)}


class BankAccountSerializer(BaseModelSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"

    expandable_fields = {"account": ("app_auth.serializers.AccountSerializer",)}


class StaffSerializer(BaseModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"

    expandable_fields = {
        "account": ("app_auth.serializers.AccountSerializer"),
        "phone_number": ("app_users.serializers.PhoneNumberSerializer"),
        "staffgroup_set": (
            "app_management.serializers.StaffGroupSerializer",
            {"many": True},
        ),
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
        "staffrole_set": (
            "app_management.serializers.StaffRoleSerializer",
            {"many": True},
        ),
    }


class GuardianSerializer(BaseModelSerializer):
    class Meta:
        model = Guardian
        fields = "__all__"

    expandable_fields = {
        "account": ("app_auth.serializers.AccountSerializer")
    }


class StudentSerializer(BaseModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    expandable_fields = {
        "account": ("app_auth.serializers.AccountSerializer"),
    }
