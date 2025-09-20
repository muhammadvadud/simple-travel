from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.tickets.models import BadgeModel
from core.apps.tickets.serializers.badge import CreateBadgeSerializer, ListBadgeSerializer, RetrieveBadgeSerializer


@extend_schema(tags=["badge"])
class BadgeView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = BadgeModel.objects.all()
    serializer_class = ListBadgeSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBadgeSerializer,
        "retrieve": RetrieveBadgeSerializer,
        "create": CreateBadgeSerializer,
    }
