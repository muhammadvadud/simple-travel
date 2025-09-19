from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.tickets.models import TicketorderModel, TicketsModel
from core.apps.tickets.serializers.tickets import (
    CreateTicketorderSerializer,
    CreateTicketsSerializer,
    ListTicketorderSerializer,
    ListTicketsSerializer,
    RetrieveTicketorderSerializer,
    RetrieveTicketsSerializer,
)


@extend_schema(tags=["tickets"])
class TicketsView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TicketsModel.objects.all()
    serializer_class = ListTicketsSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTicketsSerializer,
        "retrieve": RetrieveTicketsSerializer,
        "create": CreateTicketsSerializer,
    }


@extend_schema(tags=["ticketorder"])
class TicketorderView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TicketorderModel.objects.all()
    serializer_class = ListTicketorderSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTicketorderSerializer,
        "retrieve": RetrieveTicketorderSerializer,
        "create": CreateTicketorderSerializer,
    }
