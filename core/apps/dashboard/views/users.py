from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from ..permission.users import IsModeratorOrOperator
from core.apps.accounts.choices.user import RoleChoice
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from core.apps.dashboard.serializers.users import (
    RetrieveUsersSerializer,
    FullInfoUsersList,
)


@extend_schema(tags=["Dashboard-Users"])
class UsersView(BaseViewSetMixin, ModelViewSet):
    queryset = get_user_model().objects.filter(role=RoleChoice.USER).order_by("-id")
    serializer_class = FullInfoUsersList
    permission_classes = [IsModeratorOrOperator]
    http_method_names = ["get", "patch", "head", "options"]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['phone', 'email', 'first_name', 'last_name']
    action_permission_classes = {}
    action_serializer_class = {
        "list": FullInfoUsersList,
        "retrieve": RetrieveUsersSerializer,
        "partial_update": RetrieveUsersSerializer,
    }

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        pagination_queryset = self.paginate_queryset(queryset)
        serializer = FullInfoUsersList({"users": pagination_queryset})
        response = self.get_paginated_response(serializer.data)
        return response
