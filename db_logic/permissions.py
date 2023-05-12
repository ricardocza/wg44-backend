from rest_framework import permissions
from rest_framework.views import Request


class PostPermission(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        if request.method == "GET":
            return True
        return request.user.is_authenticated and request.user.is_staff
