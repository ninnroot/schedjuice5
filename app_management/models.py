from schedjuice5.models import BaseModel
from schedjuice5.validators import *

from app_users.models import Staff
from app_course.models import Course, Event
from django.db import models


class Group(BaseModel):

    name = models.CharField(max_length=256, validators=[nameValidation])
    description = models.TextField()
    parent_id = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)


class Department(BaseModel):

    name = models.CharField(max_length=256, validators=[nameValidation])
    description = models.TextField()
    parent_id = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)


class Job(BaseModel):

    name = models.CharField(max_length=256, validators=[nameValidation])
    description = models.TextField()
    credit_per_session = models.IntegerField()


class Role(BaseModel):

    name = models.CharField(max_length=256, validators=[nameValidation])


class Permission(BaseModel):

    code = models.CharField(max_length=256, validators=[nameWithNumberValidation])


class StaffGroup(BaseModel):

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


class StaffDepartment(BaseModel):

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    is_under = models.BooleanField(default=False)


class StaffCourse(BaseModel):

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)


class StaffSession(BaseModel):

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    session = models.ForeignKey(Event, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)


class StaffRole(BaseModel):

    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class GroupRole(BaseModel):

    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)


class RolePermission(BaseModel):

    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    permission = models.ForeignKey(Permission, on_delete=models.CASCADE)