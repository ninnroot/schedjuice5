from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from rest_framework.exceptions import ValidationError
from utilitas.models import BaseModel

from app_auth.managers import CustomUserManager
from app_microsoft.graph_wrapper.user import MSUser


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

    def delete(self, using=None, keep_parents=False):
        ms_user = MSUser()
        res = ms_user.delete(self.ms_id)
        if res.status_code not in range(199, 300):
            raise ValidationError({"MS_ERROR": res.json()})

        return super().delete(using, keep_parents)


class TempEmail(BaseModel):
    account = models.ForeignKey(
        Account, on_delete=models.CASCADE, related_name="temp_emails"
    )
    email = models.EmailField(unique=True)
