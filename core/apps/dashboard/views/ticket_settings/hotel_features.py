from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema

from core.apps.dashboard.filters import HotelFeatureFilter
from core.apps.tickets.models import HotelFeatureModel, HotelFeatureTypeModel
from core.apps.dashboard.permission.general_permission import IsModerator
from django_filters.rest_framework import DjangoFilterBackend
from core.apps.dashboard.serializers.ticket_settings.hotel_features import (
    ListHotelFeatureSerializer, CreateHotelFeatureSerializer, RetrieveHotelFeatureSerializer,
    HotelFeatureTypeSerializer
)


@extend_schema(tags=["Ticket Settings Hotel Features"])
class HotelFeatureViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = HotelFeatureModel.objects.all()
    serializer_class = ListHotelFeatureSerializer
    permission_classes = [IsModerator]
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFeatureFilter
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListHotelFeatureSerializer,
        "retrieve": RetrieveHotelFeatureSerializer,
        "create": CreateHotelFeatureSerializer,
        "partial_update": RetrieveHotelFeatureSerializer,
    }


@extend_schema(tags=["Ticket Settings Hotel Features Type"])
class HotelFeatureTypeViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = HotelFeatureTypeModel.objects.all()
    serializer_class = HotelFeatureTypeSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": HotelFeatureTypeSerializer,
        "create": HotelFeatureTypeSerializer,
        "partial_update": HotelFeatureTypeSerializer,
    }
