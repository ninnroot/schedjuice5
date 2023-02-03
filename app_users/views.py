from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication

from app_management import permissions
from schedjuice5.views import BaseDetailsView, BaseListView, BaseSearchView

from .serializers import *


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
    authentication_classes = [JWTStatelessUserAuthentication]
    permission_classes = [IsAuthenticated, permissions.Admin, permissions.Director]


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
