from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from ..permission.users import IsModeratorOrOperator
from core.apps.dashboard.serializers.users import (
    ListUsersSerializer,
    RetrieveUsersSerializer,
)


@extend_schema(tags=["Dashboard-Users"])
class UsersView(BaseViewSetMixin, ModelViewSet):
    queryset = get_user_model()
    serializer_class = ListUsersSerializer
    permission_classes = [IsModeratorOrOperator]
    http_method_names = ["get", "patch", "delete"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListUsersSerializer,
        "retrieve": RetrieveUsersSerializer,
    }
