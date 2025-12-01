from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from core.apps.tickets.models import Region
from core.apps.dashboard.permission import IsModerator, IsModeratorOrTourAdminOrOperator
from django_filters.rest_framework import DjangoFilterBackend
from core.apps.dashboard.filters.countries import RegionFilter
from core.apps.dashboard.serializers.ticket_settings.region import (
    ListRegionSerializer, RetrieveRegionSerializer, CreateRegionSerializer, UpdateRegionSerializer
)


@extend_schema(tags=["Ticket Settings Region"])
class RegionViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = Region.objects.all().order_by("-id")
    serializer_class = ListRegionSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]
    filterset_class = RegionFilter
    filter_backends = [DjangoFilterBackend]

    action_permission_classes = {
        "list": [IsModeratorOrTourAdminOrOperator],
        "retrieve": [IsModeratorOrTourAdminOrOperator]
    }
    action_serializer_class = {
        "list": ListRegionSerializer,
        "retrieve": RetrieveRegionSerializer,
        "create": CreateRegionSerializer,
        "partial_update": UpdateRegionSerializer,
    }
