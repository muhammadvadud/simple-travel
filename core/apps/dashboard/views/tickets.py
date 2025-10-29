from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.tickets.models.tickets import TicketsModel
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from ..permission.tickets import IsModeratorOrTourAdmin
from ..serializers.tickets import ListTicketsSerializer, RetrieveTicketsSerializer, CreateTicketsSerializer, \
    UpdateTicketsSerializer
from core.apps.accounts.choices import RoleChoice
from ..filters.ticket import TicketFilter


@extend_schema(tags=["Dashboard-Tickets"])
class TicketsViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = TicketsModel.objects.all()
    serializer_class = ListTicketsSerializer
    permission_classes = [IsModeratorOrTourAdmin]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TicketFilter
    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTicketsSerializer,
        "retrieve": RetrieveTicketsSerializer,
        "create": CreateTicketsSerializer,
        "partial_update": UpdateTicketsSerializer,
    }

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, "role") and user.role == RoleChoice.TourAdmin:
            return TicketsModel.objects.filter(created_by=user)

        return TicketsModel.objects.all()
