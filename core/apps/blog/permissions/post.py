from rest_framework import permissions


class PostPermission(permissions.BasePermission):

    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        return True


class TagPermission(permissions.BasePermission):

    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        return True


class CategoryPermission(permissions.BasePermission):

    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        return True


class PostimagesPermission(permissions.BasePermission):

    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
        return True


from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsModeratorOrReadOnly(BasePermission):
    """
    Moderator foydalanuvchilar uchun to‘liq ruxsat,
    qolganlar faqat o‘qishi mumkin.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_authenticated and request.user.role == "moderator")
