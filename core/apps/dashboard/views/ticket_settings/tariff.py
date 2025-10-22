from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from core.apps.tickets.models import TariffModel
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.dashboard.serializers.ticket_settings.tariff import (
    ListTariffSerializer, CreateTariffSerializer, RetrieveTariffSerializer
)


@extend_schema(tags=["Ticket Settings Tariff"])
class TicketTariffViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = TariffModel.objects.all()
    serializer_class = ListTariffSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTariffSerializer,
        "retrieve": RetrieveTariffSerializer,
        "create": CreateTariffSerializer,
        "partial_update": RetrieveTariffSerializer,
    }
