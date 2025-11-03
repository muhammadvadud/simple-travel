from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.dashboard.models import OrderStatusHistoryModel
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from ...filters.order_updated_history.order_status_history import OrderStatusHistoryFilter
from ...permission.general_permission import IsAllAdmins
from ...serializers import ListOrderStatusHistorySerializer, RetrieveOrderStatusHistorySerializer, \
    CreateOrderStatusHistorySerializer


@extend_schema(tags=["Dashboard-Order-Status-History-Payments"])
class OrderStatusHistoryPaymentsViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = OrderStatusHistoryModel.objects.all()
    serializer_class = ListOrderStatusHistorySerializer
    permission_classes = [IsAllAdmins]
    http_method_names = ["get", "post", "head", "options"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OrderStatusHistoryFilter
    action_permission_classes = {}
    action_serializer_class = {
        "list": ListOrderStatusHistorySerializer,
        "retrieve": RetrieveOrderStatusHistorySerializer,
        "create": CreateOrderStatusHistorySerializer,
    }
