from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from core.apps.tickets.models import TariffModel
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.dashboard.serializers.ticket_settings.tariff import (
    ListDashboardTariffSerializer, CreateDashboardTariffSerializer, RetrieveDashboardTariffSerializer
)


@extend_schema(tags=["Ticket Settings Tariff"])
class TicketTariffViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = TariffModel.objects.all().order_by("-id")
    serializer_class = ListDashboardTariffSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDashboardTariffSerializer,
        "retrieve": RetrieveDashboardTariffSerializer,
        "create": CreateDashboardTariffSerializer,
        "partial_update": RetrieveDashboardTariffSerializer,
    }
