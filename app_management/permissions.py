from typing import Collection, TypedDict

from rest_framework import permissions
from rest_framework_simplejwt.authentication import JWTStatelessUserAuthentication


class Message(TypedDict):
    details: Collection[str]


class CustomBasePermission(permissions.BasePermission):
    message: Message = {"details": []}

    def set_message(self, message: Collection[str]):
        self.message["details"] = message


class Admin(CustomBasePermission):
    def has_permission(self, request, view):
        print(request.user)
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE" and obj.id == request.user.id:
            return False
        return True


class Director(CustomBasePermission):
    def has_permission(self, request, view):
        print(request.user)
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == "DELETE" and obj.id == request.user.id:
            return False
        return True
