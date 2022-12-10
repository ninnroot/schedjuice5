from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from app_auth.managers import CustomUserManager
from schedjuice5.models import BaseModel


class Account(AbstractBaseUser, BaseModel, PermissionsMixin):
    """
    The model each user must have to authenticate against with.
    """

    email = models.EmailField(
        unique=True,
        help_text="The user's email address ending in the organisation's domain.",
        error_messages={"blank": {"default": "This field is required.", "user": "Hey Studpid, How do you create an account without email?"}}
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = None
    user_permissions = None

    USERNAME_FIELD = "email"
    objects = CustomUserManager()

    def __str__(self):
        return f"<Account: {self.id} {self.email}>"


class TempEmail(BaseModel):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    email = models.EmailField(unique=True)
