from rest_framework import serializers

from app_auth.models import Account
from schedjuice5.serializers import BaseModelSerializer, BaseSerializer


class AccountSerializer(BaseModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

    expandable_fields = {
        "student": ("app_users.serializers.StudentSerializer"),
        "staff": ("app_users.serializers.StaffSerializer"),
        "guardian": ("app_users.serializers.GuardianSerializer"),
        "address_set": (
            "app_users.serializers.AddressSerializer",
            {"many": True}
        ),
        "phonenumber_set": (
            "app_users.serializers.PhoneNumberSerializer",
            {"many": True}
        ),
        "bankaccount_set": (
            "app_users.serializers.BankAccountSerializer",
            {"many": True}
        ),
    }

    def create(self, validated_data):

        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)

        user.save()

        return user


class LoginSerializer(BaseSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(max_length=256)


class RequestUpdateEmailSerializer(BaseSerializer):
    email = serializers.EmailField(required=True)
