from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from app_management import permissions
from schedjuice5.views import BaseDetailsView, BaseListView, BaseSearchView

from .serializers import *


# ------------ Address Section ------------
class AddressListView(BaseListView):
    name = "Address list view"
    model = Address
    serializer = AddressSerializer
    permission_classes = [
        permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    ]


class AddressDetailsView(BaseDetailsView):
    name = "Address details view"
    model = Address
    serializer = AddressSerializer
    permission_classes = [
        permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    ]


class AddressSearchView(BaseSearchView):
    name = "Address search view"
    model = Address
    serializer = AddressSerializer
    permission_classes = [
        permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    ]


# ------------ PhoneNumber Section ------------
class PhoneNumberListView(BaseListView):
    name = "PhoneNumber list view"
    model = PhoneNumber
    serializer = PhoneNumberSerializer
    permission_classes = [
        permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    ]


class PhoneNumberDetailsView(BaseDetailsView):
    name = "PhoneNumber details view"
    model = PhoneNumber
    serializer = PhoneNumberSerializer
    permission_classes = [
        permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    ]


class PhoneNumberSearchView(BaseSearchView):
    name = "PhoneNumber search view"
    model = PhoneNumber
    serializer = PhoneNumberSerializer
    permission_classes = [
        permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    ]


# ------------ BankAccount Section ------------
class BankAccountListView(BaseListView):
    name = "BankAccount list view"
    model = BankAccount
    serializer = BankAccountSerializer
    permission_classes = [
        permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    ]


class BankAccountDetailsView(BaseDetailsView):
    name = "BankAccount details view"
    model = BankAccount
    serializer = BankAccountSerializer
    permission_classes = [
        permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    ]


class BankAccountSearchView(BaseSearchView):
    name = "BankAccount search view"
    model = BankAccount
    serializer = BankAccountSerializer
    permission_classes = [
        permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    ]


# ------------ Staff Section ------------
class StaffListView(BaseListView):
    name = "Staff list view"
    model = Staff
    serializer = StaffSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, permissions.IsRelated]
    # authentication_classes = []
    # permission_classes = []


class StaffDetailsView(BaseDetailsView):
    name = "Staff details view"
    model = Staff
    serializer = StaffSerializer
    authentication_classes = [JWTAuthentication]
    # isAdmin | (isSelf & ReadOnly)
    permission_classes = [IsAuthenticated, permissions.IsRelated]


class StaffSearchView(BaseSearchView):
    name = "Staff search view"
    model = Staff
    serializer = StaffSerializer


# ------------ Guardian Section ------------
class GuardianListView(BaseListView):
    name = "Guardian list view"
    model = Guardian
    serializer = GuardianSerializer
    permission_classes = [
        permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    ]


class GuardianDetailsView(BaseDetailsView):
    name = "Guardian details view"
    model = Guardian
    serializer = GuardianSerializer
    permission_classes = [
        permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    ]


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
