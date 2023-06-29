import functools

from rest_framework import exceptions
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from utilitas.views import BaseDetailsView, BaseListView, BaseSearchView

from app_management import permissions
from app_management.models import Course, StudentCourse

from .serializers import *


# ------------ Address Section ------------
class AddressListView(BaseListView):
    name = "Address list view"
    model = Address
    serializer = AddressSerializer
    # permission_classes = [
    #     permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    # ]


class AddressDetailsView(BaseDetailsView):
    name = "Address details view"
    model = Address
    serializer = AddressSerializer
    # permission_classes = [
    #     permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    # ]


class AddressSearchView(BaseSearchView):
    name = "Address search view"
    model = Address
    serializer = AddressSerializer
    # permission_classes = [
    #     permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    # ]


# ------------ PhoneNumber Section ------------
class PhoneNumberListView(BaseListView):
    name = "PhoneNumber list view"
    model = PhoneNumber
    serializer = PhoneNumberSerializer
    # permission_classes = [
    #     permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    # ]


class PhoneNumberDetailsView(BaseDetailsView):
    name = "PhoneNumber details view"
    model = PhoneNumber
    serializer = PhoneNumberSerializer
    # permission_classes = [
    #     permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    # ]


class PhoneNumberSearchView(BaseSearchView):
    name = "PhoneNumber search view"
    model = PhoneNumber
    serializer = PhoneNumberSerializer
    # permission_classes = [
    #     permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    # ]


# ------------ BankAccount Section ------------
class BankAccountListView(BaseListView):
    name = "BankAccount list view"
    model = BankAccount
    serializer = BankAccountSerializer
    # permission_classes = [
    #     permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    # ]


class BankAccountDetailsView(BaseDetailsView):
    name = "BankAccount details view"
    model = BankAccount
    serializer = BankAccountSerializer
    # permission_classes = [
    #     permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    # ]


class BankAccountSearchView(BaseSearchView):
    name = "BankAccount search view"
    model = BankAccount
    serializer = BankAccountSerializer
    # permission_classes = [
    #     permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    # ]


# ------------ Staff Section ------------
class StaffListView(BaseListView):
    name = "Staff list view"
    model = Staff
    serializer = StaffSerializer
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated, permissions.IsRelated]
    # authentication_classes = []
    # permission_classes = []


class StaffDetailsView(BaseDetailsView):
    name = "Staff details view"
    model = Staff
    serializer = StaffSerializer
    # authentication_classes = [JWTAuthentication]
    # isAdmin | (isSelf & ReadOnly)
    # permission_classes = [IsAuthenticated, permissions.IsRelated]


class StaffSearchView(BaseSearchView):
    name = "Staff search view"
    model = Staff
    serializer = StaffSerializer


# ------------ Guardian Section ------------
class GuardianListView(BaseListView):
    name = "Guardian list view"
    model = Guardian
    serializer = GuardianSerializer
    # permission_classes = [
    #     permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    # ]


class GuardianDetailsView(BaseDetailsView):
    name = "Guardian details view"
    model = Guardian
    serializer = GuardianSerializer
    # permission_classes = [
    #     permissions.IsAdmin | (permissions.IsRelated & permissions.ReadOnly)
    # ]


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

    @staticmethod
    def my_or(lst):
        return functools.reduce(lambda a, b: a | b, lst, True)

    def post(self, request):
        if request.query_params.get("bulk_search"):
            if not (request.data.get("emails")):
                raise exceptions.ValidationError(
                    {"non_field_errors": "'emails' is a required field."}
                )
            if not (request.data.get("course_id")):
                raise exceptions.ValidationError(
                    {"course_id": "'course_id' is a required field."}
                )

            try:
                int(request.data.get("course_id"))
            except ValueError as e:
                raise exceptions.ValidationError({"course_id": str(e)})
            course_id = int(request.data.get("course_id"))
            course = Course.objects.filter(id=course_id).first()
            if course is None:
                raise exceptions.NotFound(
                    {"course_id": "Course with the given id does not exist."}
                )

            logical_str = ""
            for i in request.data.get("emails"):
                # ahh...this is like preventing SQL injection? idk
                i = i.replace("'", "")
                logical_str += f" OR lower(a.email) LIKE '%%{i}%%'"
            logical_str = logical_str[4 : len(logical_str) + 1]
            raw_data = Student.objects.raw(
                f"""
                select s.name, s.id, a.email as account__email, a.id as account_id from app_users_student s left join app_auth_account a on a.id = s.account_id WHERE {logical_str}  
                """
            )
            existing_students = (
                StudentCourse.objects.filter(course_id=course_id)
                .prefetch_related("student")
                .all()
            )
            final_data = (
                Student.objects.filter(id__in=[i.id for i in raw_data])
                .exclude(id__in=[i.student.id for i in existing_students])
                .prefetch_related("account")
            )

            return self.send_response(
                False,
                "ok",
                {
                    "data": StudentSerializer(
                        final_data,
                        many=True,
                        fields=["id", "name", "account.email"],
                        expand=["account"],
                    ).data
                },
            )

        return super().post(request)
