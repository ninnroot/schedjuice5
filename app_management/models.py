from django.db import models

from app_course.models import Course, Event
from app_users.models import Staff, Student
from schedjuice5.models import BaseModel
from schedjuice5.validators import *

from .managers import *


class Group(BaseModel):
    """
    A Group is a collection of Staff. A Group can also contain other Groups. The relationships between Groups are
    represented by an adjacency list.
    """

    name = models.CharField(max_length=256, validators=[nameValidation], unique=True)
    description = models.TextField(default="...")
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        help_text="The parent group of the current group.",
        related_name="sub_groups",
    )

    objects = CustomCTEManager()


class Department(BaseModel):
    """
    A Department is a special kind of Group. Every Staff assignment to a Department must also contain a job_id.
    Similarly to Groups, a Department can also contain many other Departments. The inter-departmental relationships are
    represented in an adjacency list.
    """

    name = models.CharField(max_length=256, validators=[nameValidation], unique=True)
    description = models.TextField(default="...")
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        help_text="The parent department of the current department.",
        related_name="sub_departments",
    )

    objects = CustomCTEManager()


class Job(BaseModel):
    """
    A Job that a Staff can get assigned in a particular department.
    """

    name = models.CharField(max_length=256, validators=[nameValidation], unique=True)
    description = models.TextField(default="...")
    credit_per_session = models.PositiveIntegerField(
        help_text="The monetary value the job generates for the assigned Staff per assigned Event."
    )


class Role(BaseModel):
    """
    A Role is a collection of Permission. A Role can be assigned to many Staff members.
    """

    name = models.CharField(max_length=256, validators=[nameValidation], unique=True)


class Permission(BaseModel):
    """
    A Permission usually represents a boolean value on an authorization of a certain action.
    Many Permissions may be assigned to a Role which can then be assigned to a Staff. However,
    Permissions may not be assigned to a Staff directly.
    """

    code = models.CharField(max_length=256, validators=[usernameValidation])


class StaffGroup(BaseModel):
    """
    A bridge table for Staff and Group models.
    """

    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="staffs_groups"
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="staffs_groups"
    )

    class Meta:
        unique_together = ("staff", "group")


class StaffDepartment(BaseModel):
    """
    A bridge table for Staff and Department models. In each relation, a unique Job can be assigned.
    A StaffDeparment relation may also be under another StaffDepartment, thus forming a hierarchy of Staff
    within individual Departments.
    """

    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="staffs_depts"
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="staffs_depts"
    )
    job = models.ForeignKey(
        Job,
        on_delete=models.PROTECT,
        help_text="The job that the Staff does in this particular relation.",
        related_name="staffs_departments",
    )
    is_under = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        help_text="The Staff that the current staff is under the authority of.",
        related_name="sub_staffs_departments",
    )

    class Meta:
        unique_together = ("staff", "department")


class StaffCourse(BaseModel):
    """
    A bridge table for Staff and Course models. In each relation, a unique Job can be assigned.
    """

    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="staffs_courses"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="staffs_courses"
    )
    job = models.ForeignKey(
        Job, on_delete=models.PROTECT, related_name="staffs_courses"
    )

    class Meta:
        unique_together = ("staff", "course")


class StaffEvent(BaseModel):
    """
    A bridge table for Staff and Event models. In each relation, a unique Job can be assigned.
    """

    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="staffs_events"
    )
    event = models.ForeignKey(
        Event, on_delete=models.CASCADE, related_name="staffs_events"
    )
    job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name="staffs_events")

    class Meta:
        unique_together = ("staff", "event")


class StaffRole(BaseModel):
    """
    A bridge table for Staff and Role models.
    """

    staff = models.ForeignKey(
        Staff, on_delete=models.CASCADE, related_name="staffs_roles"
    )
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="staffs_roles"
    )

    class Meta:
        unique_together = ("staff", "role")


class StudentCourse(BaseModel):
    """
    A bridge table for Student and Course models.
    """

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="students_courses"
    )
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, related_name="students_courses"
    )

    class Meta:
        unique_together = ("student", "course")


class GroupRole(BaseModel):
    """
    A bridge table for Group and Role models.
    """

    group = models.ForeignKey(
        Group, on_delete=models.CASCADE, related_name="groups_roles"
    )
    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="groups_roles"
    )

    class Meta:
        unique_together = ("group", "role")


class RolePermission(BaseModel):
    """
    A bridge table for Role and Permission models.
    """

    role = models.ForeignKey(
        Role, on_delete=models.CASCADE, related_name="roles_permissions"
    )
    permission = models.ForeignKey(
        Permission, on_delete=models.CASCADE, related_name="roles_permissions"
    )

    class Meta:
        unique_together = ("role", "permission")
