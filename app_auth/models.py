from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from app_auth.managers import CustomUserManager


class Account(AbstractBaseUser, PermissionsMixin):
    """
    The model each user must have to authenticate against with.
    """

    email = models.EmailField(
        unique=True,
        help_text="The user's email address ending in the organisation's domain.",
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    objects = CustomUserManager()
