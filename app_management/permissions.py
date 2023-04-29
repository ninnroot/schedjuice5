from typing import Collection, TypedDict

from rest_framework import permissions

from app_auth.models import Account
from app_users.models import Guardian, Staff, Student


class Message(TypedDict):
    details: Collection[str]


class CustomBasePermission(permissions.BasePermission):
    message: Message = {"details": []}

    def set_message(self, message: Collection[str]):
        self.message["details"] = message


class ReadOnly(CustomBasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAdmin(CustomBasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user, "staff"):
            if "admin" in request.user.staff.roles:
                return True

        return False

    def has_object_permission(self, request, view, obj):
        if hasattr(request.user, "staff"):
            if "admin" in request.user.staff.roles:
                return True
        return False


def belongs_to(user_id: int, model, obj_id):
    x = None
    if model is Staff:
        x = model.objects.filter(account_id=user_id).first().id
    if x == obj_id:
        return True
    return False


class IsRelated(CustomBasePermission):
    def has_object_permission(self, request, view, obj):

        if belongs_to(request.user.id, view.model, obj.id):
            return True
        self.set_message("you can't read.")
        return False
