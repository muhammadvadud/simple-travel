from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices.user import RoleChoice
from ..permission.general_permission import IsModerator
from ..serializers.employees import ListEmployeesSerializer, CreateEmployeesSerializer, RetrieveEmployeesSerializer


@extend_schema(tags=["Dashboard-Employees"])
class EmployeesViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = get_user_model().objects.filter(role__in=[RoleChoice.Moderator, RoleChoice.Operator])
    serializer_class = ListEmployeesSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListEmployeesSerializer,
        "retrieve": RetrieveEmployeesSerializer,
        "create": CreateEmployeesSerializer,
    }
