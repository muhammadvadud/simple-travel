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
