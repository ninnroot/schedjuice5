import jsonschema
from django.core.exceptions import ValidationError
from django.db import models
from utilitas.models import BaseModel

import schedjuice5.config as config
from app_auth.models import Account
from app_utils.choices.careers import careers
from app_utils.choices.country_codes import country_codes
from app_utils.choices.dial_codes import dial_codes
from app_utils.choices.regions import regions
from schedjuice5.validators import *


class BaseUser(BaseModel):
    username = models.CharField(
        max_length=256, validators=[usernameValidation], null=True, blank=True
    )
    name = models.CharField(max_length=256, validators=[nameValidation])
    about = models.TextField(default="tell us something about yourself ...")
    dob = models.DateField()
    gender = models.CharField(max_length=128)

    secondary_email = models.EmailField(null=True)

    class Meta(BaseModel.Meta):
        abstract = True


class Staff(BaseUser):
    """
    One of the most fundamental models in the API. Represents a Staff user in the system.
    """

    roles_schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "type": "array",
        "items": {
            "type": "string",
            "enum": [
                "admin",
                "director",
                "coordinator",
                "main-teacher",
                "assistant-teacher",
            ],
        },
    }

    avatar = models.ImageField(
        default=config.default_avatar, upload_to=config.staff_avatar
    )
    formal_photo = models.ImageField(
        default=config.default_formal, upload_to=config.staff_formal
    )
    roles = models.JSONField(default=["assistant-teacher"])
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    class Meta(BaseUser.Meta):
        pass

    def save(self, *args, **kwargs):
        try:
            jsonschema.validate(self.roles, self.roles_schema)
        except jsonschema.exceptions.ValidationError as e:
            raise ValidationError({"roles": e.message})
        return super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        self.account.delete()
        return super().delete(using, keep_parents)


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
        max_length=128, choices=config.guardian_type_choices, null=True
    )
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    class Meta(BaseUser.Meta):
        pass

    def delete(self, using=None, keep_parents=False):
        self.account.delete()
        return super().delete(using, keep_parents)


class PhoneNumber(BaseModel):
    dial_code = models.CharField(max_length=50, choices=dial_codes)
    number = models.CharField(max_length=20)
    is_primary = models.BooleanField(default=False)
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="phone_numbers"
    )

    class Meta:
        unique_together = ("dial_code", "number")


class BankAccount(BaseModel):
    """
    A BankAccount of a user. A user may have many BankAccounts, however,
    a BankAccount can belong to one and only one user.
    """

    owner_name = models.CharField(max_length=256, validators=[nameValidation])
    number = models.CharField(max_length=256, validators=[bankAccountNumberValidation])
    bank_type = models.CharField(max_length=256, choices=config.bank_account_choices)
    save_name = models.CharField(
        max_length=256,
        validators=[englishAndSomeSpecialValidation],
        help_text="The name to save the current BankAccount as.",
        default="my_bankaccount",
    )
    is_primary = models.BooleanField(
        default=False,
        help_text="A flag for whether current BankAccount is a primary one or not.",
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, null=True, related_name="bank_accounts"
    )

    chosen_one_fields = ["is_primary"]

    class Meta(BaseModel.Meta):
        unique_together = [
            ["account", "save_name"],
        ]


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
    region = models.CharField(max_length=100, choices=regions)
    postal_code = models.CharField(max_length=16, validators=[strictNumberValidation])
    save_name = models.CharField(
        max_length=256,
        validators=[englishAndSomeSpecialValidation],
        help_text="The name to save the current Address as.",
        default="my_address",
    )
    is_primary = models.BooleanField(
        default=False,
        help_text="A flag for whether current Address is a primary one or not.",
    )
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, null=True, related_name="addresses"
    )

    chosen_one_fields = ["is_primary"]

    class Meta(BaseModel.Meta):
        unique_together = [
            ["account", "save_name"],
        ]
