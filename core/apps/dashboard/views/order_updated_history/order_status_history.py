from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.dashboard.models import OrderStatusHistoryModel
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices.user import RoleChoice
from ...permission.general_permission import IsAllAdmins
from ...serializers import ListOrderStatusHistorySerializer, RetrieveOrderStatusHistorySerializer, \
    CreateOrderStatusHistorySerializer


@extend_schema(tags=["Dashboard-Order-Status-History-Payments"])
class OrderStatusHistoryPaymentsViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = OrderStatusHistoryModel.objects.all()
    serializer_class = ListOrderStatusHistorySerializer
    permission_classes = [IsAllAdmins]
    http_method_names = ["get", "post", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOrderStatusHistorySerializer,
        "retrieve": RetrieveOrderStatusHistorySerializer,
        "create": CreateOrderStatusHistorySerializer,
    }
