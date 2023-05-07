from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from utilitas.models import BaseModel

from app_auth.managers import CustomUserManager


class Account(AbstractBaseUser, BaseModel, PermissionsMixin):
    """
    The model each user must have to authenticate against with.
    """

    email = models.EmailField(
        unique=True,
        help_text="The user's email address ending in the organisation's domain.",
        error_messages={"blank": {"default": "This field is required."}},
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    ms_id = models.CharField(max_length=128)

    groups = None
    user_permissions = None

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return f"<Account: {self.id} {self.email}>"


class TempEmail(BaseModel):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="temp_emails"
    )
    email = models.EmailField(unique=True)
