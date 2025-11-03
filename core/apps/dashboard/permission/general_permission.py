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


class IsModeratorOrTourAdminOrOperator(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in (RoleChoice.Moderator, RoleChoice.TourAdmin,
                                                                   RoleChoice.Operator):
            return True
        return False


class IsModeratorOrBuxgalter(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in (RoleChoice.Moderator,
                                                                   RoleChoice.Buxgalter):
            return True
        return False


class IsModeratorOrTourAdminOrBuxgalter(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in (RoleChoice.Moderator, RoleChoice.TourAdmin,
                                                                   RoleChoice.Buxgalter):
            return True
        return False


class IsAllAdmins(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role in (RoleChoice.Moderator, RoleChoice.Buxgalter,
                                                                   RoleChoice.TourAdmin, RoleChoice.Operator):
            return True
        return False


class IsTourAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == RoleChoice.TourAdmin:
            return True
        return False
