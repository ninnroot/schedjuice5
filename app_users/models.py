from django.db import models
from schedjuice5.models import BaseModel
from app_auth.models import Account
from schedjuice5.validators import *


class BaseUser(BaseModel):
    username = models.CharField(
        max_length=256,
        unique=True,
        validators=[usernameValidation],
    )
    name = models.CharField(max_length=256)
    about = models.TextField(default="tell us something about yourself ...")
    dob = models.DateField()
    gender = models.CharField(max_length=128)

    secondary_email = models.EmailField(null=True)
    primary_phone_number = models.CharField(
        max_length=256,
        validators=[phoneNumberValidation],
    )
    secondary_phone_number = models.CharField(
        max_length=256, null=True, validators=[phoneNumberValidation]
    )

    avatar = models.ImageField(
        default="system/default_staff_profile.jpg", upload_to="staff/avatars"
    )

    class Meta:
        abstract = True


class BankAccount(BaseModel):

    owner_name = models.CharField(max_length=256, validators=[nameValidation])
    number = models.CharField(max_length=256, validators=[bankAccountNumberValidation])
    bank_type = models.CharField(
        max_length=256,
        choices=(("KBZ", "KBZ"), ("Kpay", "Kpay"), ("AYA", "AYA"), ("CB", "CB")),
    )


class Address(BaseModel):

    house_number = models.CharField(
        max_length=16, validators=[englishAndSomeSpecialValidation]
    )
    block_number = models.CharField(
        max_length=16, validators=[englishAndSomeSpecialValidation], null=True
    )
    street_name = models.CharField(max_length=32, validators=[nameWithNumberValidation])
    township = models.CharField(max_length=32, validators=[nameWithNumberValidation])
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64)
    postal_code = models.CharField(16, validators=[strictNumberValidation])


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


class StaffBankAccount(BaseModel):
    save_name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    is_primary = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    bank_account = models.OneToOneField(BankAccount, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("staff", "bank_account")


class StaffAddress(BaseModel):
    save_name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    is_primary = models.BooleanField(default=False)
    address_type = models.CharField(max_length=128)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("staff", "address")


class StudentBankAccount(BaseModel):
    save_name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    is_primary = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bank_account = models.OneToOneField(BankAccount, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("student", "bank_account")


class StudentAddress(BaseModel):
    save_name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    is_primary = models.BooleanField(default=False)
    address_type = models.CharField(max_length=128)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("student", "address")
