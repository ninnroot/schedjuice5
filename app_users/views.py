from schedjuice5.views import BaseDetailsView, BaseListView, BaseSearchView
from .serializers import *
from .models import Staff

# ------------ Address Section ------------
class AddressListView(BaseListView):
    name = "Address list view"
    model = Address
    serializer = AddressSerializer


class AddressDetailsView(BaseDetailsView):
    name = "Address details view"
    model = Address
    serializer = AddressSerializer


class AddressSearchView(BaseSearchView):
    name = "Address search view"
    model = Address
    serializer = AddressSerializer


# ------------ PhoneNumber Section ------------
class PhoneNumberListView(BaseListView):
    name = "PhoneNumber list view"
    model = PhoneNumber
    serializer = PhoneNumberSerializer


class PhoneNumberDetailsView(BaseDetailsView):
    name = "PhoneNumber details view"
    model = PhoneNumber
    serializer = PhoneNumberSerializer


class PhoneNumberSearchView(BaseSearchView):
    name = "PhoneNumber search view"
    model = PhoneNumber
    serializer = PhoneNumberSerializer


# ------------ BankAccount Section ------------
class BankAccountListView(BaseListView):
    name = "BankAccount list view"
    model = BankAccount
    serializer = BankAccountSerializer


class BankAccountDetailsView(BaseDetailsView):
    name = "BankAccount details view"
    model = BankAccount
    serializer = BankAccountSerializer


class BankAccountSearchView(BaseSearchView):
    name = "BankAccount search view"
    model = BankAccount
    serializer = BankAccountSerializer


# ------------ Staff Section ------------
class StaffListView(BaseListView):
    name = "Staff list view"
    model = Staff
    serializer = StaffSerializer


class StaffDetailsView(BaseDetailsView):
    name = "Staff details view"
    model = Staff
    serializer = StaffSerializer


class StaffSearchView(BaseSearchView):
    name = "Staff search view"
    model = Staff
    serializer = StaffSerializer


# ------------ Guardian Section ------------
class GuardianListView(BaseListView):
    name = "Guardian list view"
    model = Guardian
    serializer = GuardianSerializer


class GuardianDetailsView(BaseDetailsView):
    name = "Guardian details view"
    model = Guardian
    serializer = GuardianSerializer


class GuardianSearchView(BaseSearchView):
    name = "Guardian search view"
    model = Guardian
    serializer = GuardianSerializer


# ------------ Student Section ------------
class StudentListView(BaseListView):
    name = "Student list view"
    model = Student
    serializer = StudentSerializer


class StudentDetailsView(BaseDetailsView):
    name = "Student details view"
    model = Student
    serializer = StudentSerializer


class StudentSearchView(BaseSearchView):
    name = "Student search view"
    model = Student
    serializer = StudentSerializer


# ------------ StaffBankAccount Section ------------
class StaffBankAccountListView(BaseListView):
    name = "StaffBankAccount list view"
    model = StaffBankAccount
    serializer = StaffBankAccountSerializer


class StaffBankAccountDetailsView(BaseDetailsView):
    name = "StaffBankAccount details view"
    model = StaffBankAccount
    serializer = StaffBankAccountSerializer


class StaffBankAccountSearchView(BaseSearchView):
    name = "StaffBankAccount search view"
    model = StaffBankAccount
    serializer = StaffBankAccountSerializer


# ------------ StaffAddress Section ------------
class StaffAddressListView(BaseListView):
    name = "StaffAddress list view"
    model = StaffAddress
    serializer = StaffAddressSerializer


class StaffAddressDetailsView(BaseDetailsView):
    name = "StaffAddress details view"
    model = StaffAddress
    serializer = StaffAddressSerializer


class StaffAddressSearchView(BaseSearchView):
    name = "StaffAddress search view"
    model = StaffAddress
    serializer = StaffAddressSerializer


# ------------ StudentBankAccount Section ------------
class StudentBankAccountListView(BaseListView):
    name = "StudentBankAccount list view"
    model = StudentBankAccount
    serializer = StudentBankAccountSerializer


class StudentBankAccountDetailsView(BaseDetailsView):
    name = "StudentBankAccount details view"
    model = StudentBankAccount
    serializer = StudentBankAccountSerializer


class StudentBankAccountSearchView(BaseSearchView):
    name = "StudentBankAccount search view"
    model = StudentBankAccount
    serializer = StudentBankAccountSerializer


# ------------ StudentAddress Section ------------
class StudentAddressListView(BaseListView):
    name = "StudentAddress list view"
    model = StudentAddress
    serializer = StudentAddressSerializer


class StudentAddressDetailsView(BaseDetailsView):
    name = "StudentAddress details view"
    model = StudentAddress
    serializer = StudentAddressSerializer


class StudentAddressSearchView(BaseSearchView):
    name = "StudentAddress search view"
    model = StudentAddress
    serializer = StudentAddressSerializer

