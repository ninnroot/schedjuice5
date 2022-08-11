from django.db import models
from schedjuice5.models import BaseModel
from app_auth.models import Account
from schedjuice5.validators import *
import schedjuice5.config as config

from app_utils.choices import careers, countries


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

    class Meta(BaseModel.Meta):
        abstract = True


class BankAccount(BaseModel):

    owner_name = models.CharField(max_length=256, validators=[nameValidation])
    number = models.CharField(max_length=256, validators=[bankAccountNumberValidation])
    bank_type = models.CharField(max_length=256, choices=config.bank_account_choices)

    class Meta(BaseModel.Meta):
        pass


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
    country = models.CharField(max_length=64, choices=countries)
    postal_code = models.CharField(max_length=16, validators=[strictNumberValidation])

    class Meta(BaseModel.Meta):
        pass


class Staff(BaseUser):
    avatar = models.ImageField(
        default=config.default_avatar, upload_to=config.staff_avatar
    )
    formal_photo = models.ImageField(
        default=config.default_formal, upload_to=config.staff_formal
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta(BaseUser.Meta):
        pass


class Guardian(BaseUser):

    avatar = models.ImageField(
        default=config.default_avatar, upload_to=config.guardian_avatar
    )
    career = models.CharField(max_length=512, choices=careers)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta(BaseUser.Meta):
        pass


class Student(BaseUser):
    avatar = models.ImageField(
        default=config.default_avatar, upload_to=config.student_avatar
    )
    formal_photo = models.ImageField(
        default=config.default_formal,
        upload_to=config.student_formal,
    )
    guardian_type = models.CharField(
        max_length=128,
        choices=config.guardian_type_choices,
    )
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta(BaseUser.Meta):
        pass


class StaffBankAccount(BaseModel):
    save_name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    is_primary = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    bank_account = models.OneToOneField(BankAccount, on_delete=models.CASCADE)

    chosen_one_fields = ["is_primary"]

    class Meta(BaseModel.Meta):
        unique_together = ("staff", "bank_account")


class StaffAddress(BaseModel):
    save_name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    is_primary = models.BooleanField(default=False)
    address_type = models.CharField(max_length=128)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    chosen_one_fields = ["is_primary"]

    class Meta(BaseModel.Meta):
        unique_together = ("staff", "address")


class StudentBankAccount(BaseModel):
    save_name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    is_primary = models.BooleanField(default=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bank_account = models.OneToOneField(BankAccount, on_delete=models.CASCADE)

    chosen_one_fields = ["is_primary"]

    class Meta(BaseModel.Meta):
        unique_together = ("student", "bank_account")


class StudentAddress(BaseModel):
    save_name = models.CharField(
        max_length=256, validators=[englishAndSomeSpecialValidation]
    )
    is_primary = models.BooleanField(default=False)
    address_type = models.CharField(max_length=128)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    chosen_one_fields = ["is_primary"]

    class Meta(BaseModel.Meta):
        unique_together = ("student", "address")
