from schedjuice5.serializers import BaseModelSerializer

from .models import *


class AddressSerializer(BaseModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class PhoneNumberSerializer(BaseModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = "__all__"


class BankAccountSerializer(BaseModelSerializer):
    class Meta:
        model = BankAccount
        fields = "__all__"


class StaffSerializer(BaseModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"


class GuardianSerializer(BaseModelSerializer):
    class Meta:
        model = Guardian
        fields = "__all__"


class StudentSerializer(BaseModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


class StaffBankAccountSerializer(BaseModelSerializer):
    class Meta:
        model = StaffBankAccount
        fields = "__all__"


class StaffAddressSerializer(BaseModelSerializer):
    class Meta:
        model = StaffAddress
        fields = "__all__"


class StudentBankAccountSerializer(BaseModelSerializer):
    class Meta:
        model = StudentBankAccount
        fields = "__all__"


class StudentAddressSerializer(BaseModelSerializer):
    class Meta:
        model = StudentAddress
        fields = "__all__"
