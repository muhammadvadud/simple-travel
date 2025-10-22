from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.tickets.models.tickets import TicketsModel
from drf_spectacular.utils import extend_schema
from ..permission.tickets import IsModeratorOrTourAdmin
from ..serializers.tickets import ListTicketsSerializer, RetrieveTicketsSerializer, CreateTicketsSerializer


@extend_schema(tags=["Dashboard-Tickets"])
class TicketsViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = TicketsModel.objects.all()
    serializer_class = ListTicketsSerializer
    permission_classes = [IsModeratorOrTourAdmin]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTicketsSerializer,
        "retrieve": RetrieveTicketsSerializer,
        "create": CreateTicketsSerializer,
        "partial_update": RetrieveTicketsSerializer,
    }
