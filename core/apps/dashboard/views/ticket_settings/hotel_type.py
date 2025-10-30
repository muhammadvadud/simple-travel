from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from core.apps.tickets.models import HotelTypeModel
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.dashboard.serializers.ticket_settings.hotel_type import (
    ListHotelTypeSerializer, RetrieveHotelTypeSerializer, CreateHotelTypeSerializer
)


@extend_schema(tags=["Ticket Settings Hotel Type"])
class HotelTypeViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = HotelTypeModel.objects.all().order_by("-id")
    serializer_class = ListHotelTypeSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListHotelTypeSerializer,
        "retrieve": RetrieveHotelTypeSerializer,
        "create": CreateHotelTypeSerializer,
        "partial_update": RetrieveHotelTypeSerializer,
    }
