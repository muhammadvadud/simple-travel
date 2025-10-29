from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.tickets.models.tickets import TicketorderModel
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices.user import RoleChoice
from ..permission.tickets import IsModeratorOrTourAdmin
from ..serializers.ticket_order import ListTicketOrderSerializer, RetrieveTicketOrderSerializer, \
    UpdateTicketOrderSerializer


@extend_schema(tags=["Dashboard-Ticket-Order"])
class TicketOrderViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = TicketorderModel.objects.all()
    serializer_class = ListTicketOrderSerializer
    permission_classes = [IsModeratorOrTourAdmin]
    http_method_names = ["get", "patch", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTicketOrderSerializer,
        "retrieve": RetrieveTicketOrderSerializer,
        "partial_update": UpdateTicketOrderSerializer,
    }

    def get_queryset(self):
        user = self.request.user
        if hasattr(user, "role") and user.role == RoleChoice.TourAdmin:
            return TicketorderModel.objects.filter(ticket__tour__agency__id=user.travel_agency)
        return TicketorderModel.objects.all()
