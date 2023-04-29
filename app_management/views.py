import asyncio

from asgiref.sync import AsyncToSync, async_to_sync
from channels.layers import get_channel_layer
from rest_framework.views import Request, Response
from utilitas.views import BaseDetailsView, BaseListView, BaseSearchView

from .models import *
from .serializers import *


# ------------ Group Section ------------
class GroupListView(BaseListView):
    name = "Group list view"
    model = Group
    serializer = GroupSerializer


class GroupDetailsView(BaseDetailsView):
    name = "Group details view"
    model = Group
    serializer = GroupSerializer


class GroupSearchView(BaseSearchView):
    name = "Group search view"
    model = Group
    serializer = GroupSerializer


# ------------ Department Section ------------
class DepartmentListView(BaseListView):
    name = "Department list view"
    model = Department
    serializer = DepartmentSerializer


class DepartmentDetailsView(BaseDetailsView):
    name = "Department details view"
    model = Department
    serializer = DepartmentSerializer


class DepartmentSearchView(BaseSearchView):
    name = "Department search view"
    model = Department
    serializer = DepartmentSerializer


# ------------ Job Section ------------
class JobListView(BaseListView):
    name = "Job list view"
    model = Job
    serializer = JobSerializer


class JobDetailsView(BaseDetailsView):
    name = "Job details view"
    model = Job
    serializer = JobSerializer


class JobSearchView(BaseSearchView):
    name = "Job search view"
    model = Job
    serializer = JobSerializer


# ------------ Role Section ------------
class RoleListView(BaseListView):
    name = "Role list view"
    model = Role
    serializer = RoleSerializer


class RoleDetailsView(BaseDetailsView):
    name = "Role details view"
    model = Role
    serializer = RoleSerializer


class RoleSearchView(BaseSearchView):
    name = "Role search view"
    model = Role
    serializer = RoleSerializer


# ------------ Permission Section ------------
class PermissionListView(BaseListView):
    name = "Permission list view"
    model = Permission
    serializer = PermissionSerializer


class PermissionDetailsView(BaseDetailsView):
    name = "Permission details view"
    model = Permission
    serializer = PermissionSerializer


class PermissionSearchView(BaseSearchView):
    name = "Permission search view"
    model = Permission
    serializer = PermissionSerializer


# ------------ StaffGroup Section ------------
class StaffGroupListView(BaseListView):
    name = "StaffGroup list view"
    model = StaffGroup
    serializer = StaffGroupSerializer


class StaffGroupDetailsView(BaseDetailsView):
    name = "StaffGroup details view"
    model = StaffGroup
    serializer = StaffGroupSerializer


class StaffGroupSearchView(BaseSearchView):
    name = "StaffGroup search view"
    model = StaffGroup
    serializer = StaffGroupSerializer


# ------------ StaffDepartment Section ------------
class StaffDepartmentListView(BaseListView):
    name = "StaffDepartment list view"
    model = StaffDepartment
    serializer = StaffDepartmentSerializer


class StaffDepartmentDetailsView(BaseDetailsView):
    name = "StaffDepartment details view"
    model = StaffDepartment
    serializer = StaffDepartmentSerializer


class StaffDepartmentSearchView(BaseSearchView):
    name = "StaffDepartment search view"
    model = StaffDepartment
    serializer = StaffDepartmentSerializer


# ------------ StaffCourse Section ------------
class StaffCourseListView(BaseListView):
    name = "StaffCourse list view"
    model = StaffCourse
    serializer = StaffCourseSerializer


class StaffCourseDetailsView(BaseDetailsView):
    name = "StaffCourse details view"
    model = StaffCourse
    serializer = StaffCourseSerializer


class StaffCourseSearchView(BaseSearchView):
    name = "StaffCourse search view"
    model = StaffCourse
    serializer = StaffCourseSerializer


# ------------ StudentCourse Section ------------
class StudentCourseListView(BaseListView):
    name = "StudentCourse list view"
    model = StudentCourse
    serializer = StudentCourseSerializer


class StudentCourseDetailsView(BaseDetailsView):
    name = "StudentCourse details view"
    model = StudentCourse
    serializer = StudentCourseSerializer


class StudentCourseSearchView(BaseSearchView):
    name = "StudentCourse search view"
    model = StudentCourse
    serializer = StudentCourseSerializer


# ------------ StaffEvent Section ------------
class StaffEventListView(BaseListView):
    name = "StaffEvent list view"
    model = StaffEvent
    serializer = StaffEventSerializer


class StaffEventDetailsView(BaseDetailsView):
    name = "StaffEvent details view"
    model = StaffEvent
    serializer = StaffEventSerializer


class StaffEventSearchView(BaseSearchView):
    name = "StaffEvent search view"
    model = StaffEvent
    serializer = StaffEventSerializer


# ------------ StaffRole Section ------------
class StaffRoleListView(BaseListView):
    name = "StaffRole list view"
    model = StaffRole
    serializer = StaffRoleSerializer


class StaffRoleDetailsView(BaseDetailsView):
    name = "StaffRole details view"
    model = StaffRole
    serializer = StaffRoleSerializer


class StaffRoleSearchView(BaseSearchView):
    name = "StaffRole search view"
    model = StaffRole
    serializer = StaffRoleSerializer


# ------------ GroupRole Section ------------
class GroupRoleListView(BaseListView):
    name = "GroupRole list view"
    model = GroupRole
    serializer = GroupRoleSerializer


class GroupRoleDetailsView(BaseDetailsView):
    name = "GroupRole details view"
    model = GroupRole
    serializer = GroupRoleSerializer


class GroupRoleSearchView(BaseSearchView):
    name = "GroupRole search view"
    model = GroupRole
    serializer = GroupRoleSerializer


# ------------ RolePermission Section ------------
class RolePermissionListView(BaseListView):
    name = "RolePermission list view"
    model = RolePermission
    serializer = RolePermissionSerializer


class RolePermissionDetailsView(BaseDetailsView):
    name = "RolePermission details view"
    model = RolePermission
    serializer = RolePermissionSerializer


class RolePermissionSearchView(BaseSearchView):
    name = "RolePermission search view"
    model = RolePermission
    serializer = RolePermissionSerializer


class GetNestedTest(BaseListView):
    name = "test"
    model = Group
    serializer = GroupSerializer

    def get(self, request):
        x = Group.objects.get_nested()
        for i in x:
            if i.id == 20:
                print(i.parent.parent.parent.parent)

        return Response({"message": "k"})
