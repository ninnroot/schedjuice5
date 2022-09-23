from rest_framework.serializers import models

from schedjuice5.serializers import BaseModelSerializer

from .models import *


class AddressSerializer(BaseModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    expandable_fields = {
        "staffaddress_set": (
            "app_users.serializers.StaffAddressSerializer",
            {"many": True},
        ),
        "studentaddress_set": (
            "app_users.serializers.StudentAddressSerializer",
            {"many": True},
        ),
        # "guardianaddress_set": (
        #     "app_users.serializers.GuardianAddressSerializer",
        #     {"many": True},
        # ),
    }


class PhoneNumberSerializer(BaseModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = "__all__"

    expandable_fields = {
        "staff_set": ("app_users.serializers.StaffSerializer", {"many": True}),
        "student_set": ("app_users.serializers.StudentSerializer", {"many": True}),
        # "guardian_set": ("app_users.serializers.GuardianSerializer", {"many": True}),
    }


class BankAccountSerializer(BaseModelSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"

    expandable_fields = {
        "staffbankaccount": ("app_users.serializers.StaffBankAccountSerializer"),
        "studentbankaccount": ("app_users.serializers.StudentBankAccountSerializer"),
        # "guardianbankaccount": (
        #     "app_users.serializers.GuardianBankAccountSerializer"
        # ),
    }


class StaffSerializer(BaseModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"

    expandable_fields = {
        "account": ("app_auth.serializers.AccountSerializer"),
        "phone_number": ("app_users.serializers.PhoneNumberSerializer"),
        "staffbankaccount_set": (
            "app_users.serializers.StaffBankAccountSerializer",
            {"many": True},
        ),
        "staffaddress_set": (
            "app_users.serializers.StaffAddressSerializer",
            {"many": True},
        ),
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
        "account": ("app_auth.serializers.AccountSerializer"),
        # "phone_number": ("app_users.serializers.PhoneNumberSerializer"),
    }


class StudentSerializer(BaseModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"

    expandable_fields = {
        "account": ("app_auth.serializers.AccountSerializer"),
        "phone_number": ("app_users.serializers.PhoneNumberSerializer"),
        "studentbankaccount_set": (
            "app_users.serializers.StudentBankAccountSerializer",
            {"many": True},
        ),
        "studentaddress_set": (
            "app_users.serializers.StudentAddressSerializer",
            {"many": True},
        ),
    }


class StaffBankAccountSerializer(BaseModelSerializer):
    class Meta:
        model = StaffBankAccount
        fields = "__all__"

    expandable_fields = {
        "staff": ("app_users.serializers.StaffSerializer"),
        "bank_account": ("app_users.serializers.BankAccountSerializer"),
    }


class StaffAddressSerializer(BaseModelSerializer):
    class Meta:
        model = StaffAddress
        fields = "__all__"

    expandable_fields = {
        "staff": ("app_users.serializers.StaffSerializer"),
        "address": ("app_users.serializers.AddressSerializer"),
    }


class StudentBankAccountSerializer(BaseModelSerializer):
    class Meta:
        model = StudentBankAccount
        fields = "__all__"

    expandable_fields = {
        "student": ("app_users.serializers.StudentSerializer"),
        "bank_account": ("app_users.serializers.BankAccountSerializer"),
    }


class StudentAddressSerializer(BaseModelSerializer):
    class Meta:
        model = StudentAddress
        fields = "__all__"

    expandable_fields = {
        "student": ("app_users.serializers.StudentSerializer"),
        "address": ("app_users.serializers.AddressSerializer"),
    }
