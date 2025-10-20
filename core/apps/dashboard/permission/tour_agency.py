from rest_framework import permissions

from core.apps.accounts.choices import RoleChoice


class IsModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == RoleChoice.Moderator:
            return True
        else:
            return False


class IsOperatorOrModerator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (
                request.user.role == RoleChoice.Operator or
                request.user.role == RoleChoice.Moderator
        ):
            return True
        return False
