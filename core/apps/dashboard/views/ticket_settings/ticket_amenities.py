from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from core.apps.tickets.models import TicketsAmenitiesModel
from core.apps.dashboard.permission import IsModerator, IsModeratorOrTourAdmin
from core.apps.dashboard.serializers.ticket_settings import (
    ListTicketsAmenitiesSerializer, RetrieveTicketsAmenitiesSerializer, CreateTicketsAmenitiesSerializer,
)


@extend_schema(tags=["Ticket Settings Amenities"])
class TicketAmenitiesViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = TicketsAmenitiesModel.objects.all().order_by("-id")
    serializer_class = ListTicketsAmenitiesSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {
        "list": [IsModeratorOrTourAdmin],
        "retrieve": [IsModeratorOrTourAdmin],
    }
    action_serializer_class = {
        "list": ListTicketsAmenitiesSerializer,
        "retrieve": RetrieveTicketsAmenitiesSerializer,
        "create": CreateTicketsAmenitiesSerializer,
        "partial_update": RetrieveTicketsAmenitiesSerializer,
    }
