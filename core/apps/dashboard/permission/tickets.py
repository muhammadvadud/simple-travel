from rest_framework.permissions import BasePermission

from core.apps.accounts.choices import RoleChoice


class IsModeratorOrTourAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in (
                RoleChoice.Moderator,
                RoleChoice.TourAdmin,
                RoleChoice.Buxgalter,):
            return True
        return False
