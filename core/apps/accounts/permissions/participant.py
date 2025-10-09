from rest_framework import permissions


class ParticipantPermission(permissions.BasePermission):

    def __init__(self) -> None: ...

    def __call__(self, *args, **kwargs):
        return self

    def has_permission(self, request, view):
       return request.user and request.user.is_authenticated
    def has_object_permission(self, request, view, obj):
        return obj.created_by == request.user