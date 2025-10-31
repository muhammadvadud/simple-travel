from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from core.apps.tickets.models import BadgeModel
from core.apps.dashboard.permission import IsModerator,IsModeratorOrTourAdmin
from core.apps.dashboard.serializers.ticket_settings import (
    RetrieveBadgeSerializer, ListBadgeSerializer, CreateBadgeSerializer
)


@extend_schema(tags=["Ticket Settings Badge"])
class TicketBadgeViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = BadgeModel.objects.all().order_by("-id")
    serializer_class = ListBadgeSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {
        "list": [IsModeratorOrTourAdmin],
        "retrieve": [IsModeratorOrTourAdmin],
    }
    action_serializer_class = {
        "list": ListBadgeSerializer,
        "retrieve": RetrieveBadgeSerializer,
        "create": CreateBadgeSerializer,
        "partial_update": RetrieveBadgeSerializer,
    }
