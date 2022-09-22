from django.db import models

import schedjuice5.config as config
from app_auth.models import Account
from app_utils.choices.careers import careers
from app_utils.choices.country_codes import country_codes
from app_utils.choices.dial_codes import dial_codes
from schedjuice5.models import BaseModel
from schedjuice5.validators import *


class PhoneNumber(BaseModel):
    dial_code = models.CharField(max_length=50, choices=dial_codes)
    number = models.CharField(max_length=20)
    is_primary = models.BooleanField(default=False)

    class Meta:
        unique_together = ("dial_code", "number")


class BaseUser(BaseModel):
    username = models.CharField(
        max_length=256,
        unique=True,
        validators=[usernameValidation],
    )
    name = models.CharField(max_length=256, validators=[nameValidation])
    about = models.TextField(default="tell us something about yourself ...")
    dob = models.DateField()
    gender = models.CharField(max_length=128)

    secondary_email = models.EmailField(null=True)
    phone_number = models.ForeignKey(PhoneNumber, on_delete=models.CASCADE)

    class Meta(BaseModel.Meta):
        abstract = True


class BankAccount(BaseModel):
    """
    A BankAccount of a user. A user may have many BankAccounts, however,
    a BankAccount can belong to one and only one user.
    """

    owner_name = models.CharField(max_length=256, validators=[nameValidation])
    number = models.CharField(max_length=256, validators=[bankAccountNumberValidation])
    bank_type = models.CharField(max_length=256, choices=config.bank_account_choices)

    class Meta(BaseModel.Meta):
        pass


class Address(BaseModel):
    """
    An Address of a user. A user may have many Addresses, but not vice versa.
    """

    house_number = models.CharField(
        max_length=16, validators=[englishAndSomeSpecialValidation]
    )
    block_number = models.CharField(
        max_length=16, validators=[englishAndSomeSpecialValidation], null=True
    )
    street_name = models.CharField(max_length=32, validators=[nameWithNumberValidation])
    township = models.CharField(max_length=32, validators=[nameWithNumberValidation])
    city = models.CharField(max_length=64)
    country = models.CharField(max_length=64, choices=country_codes)
    postal_code = models.CharField(max_length=16, validators=[strictNumberValidation])

    class Meta(BaseModel.Meta):
        pass


class Staff(BaseUser):
    """
    One of the most fundamental models in the API. Represents a Staff user in the system.
    """

    avatar = models.ImageField(
        default=config.default_avatar, upload_to=config.staff_avatar
    )
    formal_photo = models.ImageField(
        default=config.default_formal, upload_to=config.staff_formal
    )
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    class Meta(BaseUser.Meta):
        pass


class Guardian(BaseUser):
    """
    Represents a parent or a legal guardian of a Student.
    """

    avatar = models.ImageField(
        default=config.default_avatar, upload_to=config.guardian_avatar
    )
    career = models.CharField(max_length=512, choices=careers)
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    class Meta(BaseUser.Meta):
        pass


class Student(BaseUser):
    """
    A Student user.
    """

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
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    class Meta(BaseUser.Meta):
        pass


class StaffBankAccount(BaseModel):
    """
    A bridge table for Staff and BankAccount models.
    """

    save_name = models.CharField(
        max_length=256,
        validators=[englishAndSomeSpecialValidation],
        help_text="The name to save the current BankAccount as.",
    )
    is_primary = models.BooleanField(
        default=False,
        help_text="A flag for whether current BankAccount is a primary one or not.",
    )
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    bank_account = models.OneToOneField(BankAccount, on_delete=models.CASCADE)

    chosen_one_fields = ["is_primary"]

    class Meta(BaseModel.Meta):
        unique_together = ("staff", "bank_account", "save_name")


class StaffAddress(BaseModel):
    """
    A bridge table for Staff and Address models.
    """

    save_name = models.CharField(
        max_length=256,
        validators=[englishAndSomeSpecialValidation],
        help_text="The name to save the current Address as.",
    )
    is_primary = models.BooleanField(
        default=False,
        help_text="A flag for whether current Address is a primary one or not.",
    )
    address_type = models.CharField(max_length=128)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)

    chosen_one_fields = ["is_primary"]

    class Meta(BaseModel.Meta):
        unique_together = ("staff", "address", "save_name")


class StudentBankAccount(BaseModel):
    """
    A bridge table for Student and BankAccount models.
    """

    save_name = models.CharField(
        max_length=256,
        validators=[englishAndSomeSpecialValidation],
        help_text="The name to save the current BankAccount as.",
    )
    is_primary = models.BooleanField(
        default=False,
        help_text="A flag for whether current BankAccount is a primary one or not.",
    )
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    bank_account = models.OneToOneField(BankAccount, on_delete=models.CASCADE)

    chosen_one_fields = ["is_primary"]

    class Meta(BaseModel.Meta):
        unique_together = ("student", "bank_account", "save_name")


class StudentAddress(BaseModel):
    """
    A bridge table for Student and Address models.
    """

    save_name = models.CharField(
        max_length=256,
        validators=[englishAndSomeSpecialValidation],
        help_text="The name to save the current Address as.",
    )
    is_primary = models.BooleanField(
        default=False,
        help_text="A flag for whether current Address is a primary one or not.",
    )
    address_type = models.CharField(max_length=128)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    address = models.OneToOneField(Address, on_delete=models.CASCADE)

    chosen_one_fields = ["is_primary"]

    class Meta(BaseModel.Meta):
        unique_together = ("student", "address", "save_name")
