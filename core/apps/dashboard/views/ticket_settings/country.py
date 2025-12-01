from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from core.apps.tickets.models import Country
from core.apps.dashboard.permission import IsModerator, IsModeratorOrTourAdminOrOperator
from core.apps.dashboard.serializers.ticket_settings.country import (
    ListCountrySerializer, RetrieveCountrySerializer, CreateCountrySerializer
)


@extend_schema(tags=["Ticket Settings Country"])
class CountryViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = Country.objects.all().order_by("-id")
    serializer_class = ListCountrySerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {
        "list": [IsModeratorOrTourAdminOrOperator],
        "retrieve": [IsModeratorOrTourAdminOrOperator]
    }
    action_serializer_class = {
        "list": ListCountrySerializer,
        "retrieve": RetrieveCountrySerializer,
        "create": CreateCountrySerializer,
        "partial_update": RetrieveCountrySerializer,
    }
