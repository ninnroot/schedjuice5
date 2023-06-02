import requests
from drf_writable_nested.serializers import NestedCreateMixin
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from utilitas.serializers import BaseModelSerializer, BaseSerializer

from app_auth.models import Account
from app_microsoft.flows import CreateAccountFlow
from app_users.serializers import (
    AddressSerializer,
    BankAccountSerializer,
    GuardianSerializer,
    PhoneNumberSerializer,
    StaffSerializer,
    StudentSerializer,
)


class AccountSerializer(BaseModelSerializer):
    class Meta(BaseModelSerializer.Meta):
        model = Account
        fields = "__all__"

        extra_kwargs = {"password": {"write_only": True}, "ms_id": {"required": False}}

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

        # skip the ms_account creation if that flag is set to True.
        if not self.context.get("skip_ms_creation"):
            # start the flow to create MS user.
            # if successful, a uuid will get returned.
            # if fails, it'll raise a ValidationError and Django will handle it gracefully. No need to think about it here.
            flow = CreateAccountFlow(validated_data["email"], password)
            user_id = flow.start()

            # add the uuid to user data. This will later be used to link the MS user and local user.
            validated_data["ms_id"] = user_id
        else:
            print("Skipping MS creation because of the flag.")

        # then, create a user in the local db.
        user = super().create(validated_data)
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.save()

        return user

    def update(self, instance, validated_data):
        # TODO: update password in MS
        password = validated_data.pop("password", None)

        if password:
            instance.set_password(password)
            instance.save()
        return super().update(instance, validated_data)


class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

    def validate(self, attrs):
        # TODO: customize login using MS Graph
        res = requests.get(
            "https://graph.microsoft.com/v1.0/" + "me",
            headers={
                "Authorization": "Bearer " + "",
                "Content-Type": "application/json",
            },
        )
        data = super().validate(attrs)
        if hasattr(self.user, "student"):
            data["user_type"] = "student"
            data["student_id"] = self.user.student.id
            data["account_id"] = self.user.id
            data["user"] = StudentSerializer(self.user.student).data
        elif hasattr(self.user, "staff"):
            data["user_type"] = "staff"
            data["staff_id"] = self.user.staff.id
            data["account_id"] = self.user.id
            data["user"] = StaffSerializer(self.user.staff).data
        elif hasattr(self.user, "guardian"):
            data["user_type"] = "guardian"
            data["guardian_id"] = self.user.guardian.id
            data["account_id"] = self.user.id
            data["user"] = GuardianSerializer(self.user.guardian).data
        else:
            raise serializers.ValidationError(
                {
                    "non_field_errors": [
                        "This account has no association with any type of user."
                    ]
                }
            )
        return data


def get_user_from_MS_token(ms_access: str):
    res = requests.get(
        "https://graph.microsoft.com/v1.0/" + "me",
        headers={
            "Authorization": "Bearer " + ms_access,
            "Content-Type": "application/json",
        },
    )
    if res.status_code not in range(199, 300):
        raise ValidationError({"error_type": "MS ERROR", "details": {**res.json()}})
    user_id = res.json()["id"]
    user = Account.objects.filter(ms_id=user_id).first()
    if not user:
        raise ValidationError(
            {"error_type": "MS ERROR", "details": "No such user exists in this tenant."}
        )

    return user


class MSLoginSerializer(BaseSerializer):
    token = serializers.CharField(max_length=5280)

    def validate(self, attrs):
        # we get a user instance by making a request to MS Graph API
        user = get_user_from_MS_token(attrs["token"])
        access_token = RefreshToken.for_user(user).access_token
        data = super().validate(attrs)
        if hasattr(user, "student"):
            data["user_type"] = "student"
            data["student_id"] = user.student.id
            data["account_id"] = user.id
            data["user"] = StudentSerializer(user.student).data
        elif hasattr(user, "staff"):
            data["user_type"] = "staff"
            data["staff_id"] = user.staff.id
            data["account_id"] = user.id
            data["user"] = StaffSerializer(user.staff).data
        # guardian is currently not supported yet
        # elif hasattr(self.user, "guardian"):
        #     data["user_type"] = "guardian"
        #     data["guardian_id"] = self.user.guardian.id
        #     data["account_id"] = self.user.id
        #     data["user"] = GuardianSerializer(self.user.guardian).data
        else:
            raise serializers.ValidationError(
                {
                    "non_field_errors": [
                        "This account has no association with any type of user."
                    ]
                }
            )
        return data


class RequestUpdateEmailSerializer(BaseSerializer):
    email = serializers.EmailField(required=True)
