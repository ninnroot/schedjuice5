from django.db import models
from schedjuice5.models import BaseModel
from app_auth.models import Account
from django.core.validators import RegexValidator


class BaseUser(BaseModel):
    username = models.CharField(
        max_length=256,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^[\w\d_]{8,32}$",
                message="username must match this: '^[\\w\\d_]{8,32}$'",
            )
        ],
    )
    name = models.CharField(max_length=256)
    about = models.TextField(default="tell us something about yourself ...")
    dob = models.DateField()
    gender = models.CharField(max_length=128)

    secondary_email = models.EmailField(null=True)
    primary_phone_number = models.CharField(
        max_length=256,
        validators=[
            RegexValidator(
                regex=r"^[\d+ ]{6,20}$",
                message="phone number must match this: '^[\\d+ ]{6,20}$'",
            )
        ],
    )
    secondary_phone_number = models.CharField(
        max_length=256,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^[\d+ ]{6,20}$",
                message="phone number must match this: '^[\\d+ ]{6,20}$'",
            )
        ],
    )

    avatar = models.ImageField(
        default="system/default_staff_profile.jpg", upload_to="staff/avatars"
    )

    class Meta:
        abstract = True


class Staff(BaseUser):

    formal_photo = models.ImageField(
        default="system/default_staff_formal_photo.jpg", upload_to="staff/formal_photos"
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Guardian(BaseUser):

    career = models.CharField(
        max_length=128, choices=(("teacher", "teacher"), ("engineer", "engineer"))
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)


class Student(BaseUser):

    formal_photo = models.ImageField(
        default="system/default_student_formal_photo.jpg",
        upload_to="student/formal_photos",
    )
    guardian_type = models.CharField(
        max_length=128,
        choices=(
            ("father", "father"),
            ("mother", "mother"),
            ("relative", "relative"),
            ("other", "other"),
        ),
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
