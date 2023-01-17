from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from app_auth.models import Account
from schedjuice5.serializers import BaseModelSerializer, BaseSerializer


class AccountSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Account
        fields = "__all__"

        extra_kwargs = {
            "password": {"write_only": True},
        }

    expandable_fields = {
        "student": ("app_users.serializers.StudentSerializer"),
        "staff": ("app_users.serializers.StaffSerializer"),
        "guardian": ("app_users.serializers.GuardianSerializer"),
        "addresses": ("app_users.serializers.AddressSerializer", {"many": True}),
        "phone_numbers": (
            "app_users.serializers.PhoneNumberSerializer",
            {"many": True},
        ),
        "bank_accounts": (
            "app_users.serializers.BankAccountSerializer",
            {"many": True},
        ),
    }

    def create(self, validated_data):

        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)

        user.save()

        return user


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        if hasattr(self.user, "student"):
            data["user_type"] = "student"
            data["student_id"] = self.user.student.id
            data["account_id"] = self.user.id
        elif hasattr(self.user, "staff"):
            data["user_type"] = "staff"
            data["staff_id"] = self.user.staff.id
            data["account_id"] = self.user.id
        elif hasattr(self.user, "guardian"):
            data["user_type"] = "guardian"
            data["guardian_id"] = self.user.guardian.id
            data["account_id"] = self.user.id

        return data


class RequestUpdateEmailSerializer(BaseSerializer):
    email = serializers.EmailField(required=True)
