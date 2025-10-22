from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from core.apps.tickets.models import TransportTicketModel
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.dashboard.serializers.ticket_settings.ticket_transports import (
    ListTransportSerializer, RetrieveTransportSerializer, CreateTransportSerializer
)


@extend_schema(tags=["Ticket Settings Transport"])
class TicketTransportViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = TransportTicketModel.objects.all()
    serializer_class = ListTransportSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTransportSerializer,
        "retrieve": RetrieveTransportSerializer,
        "create": CreateTransportSerializer,
        "partial_update": RetrieveTransportSerializer,
    }
