from rest_framework.permissions import BasePermission

from core.apps.accounts.choices import RoleChoice


class IsModerator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == RoleChoice.Moderator:
            return True
        return False


class IsOperator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == RoleChoice.Moderator:
            return True
        return False
