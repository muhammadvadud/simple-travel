from rest_framework import permissions
from core.apps.accounts.choices.user import RoleChoice


class IsModeratorOrOperator(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and (
                request.user.role == RoleChoice.Moderator or
                request.user.role == RoleChoice.Operator
        ):
            return True
        return False
