from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.tickets.models import ExtraServicesModel, PaidServicesModel
from core.apps.tickets.serializers.extra_services import (
    CreateExtraServicesSerializer,
    CreatePaidServicesSerializer,
    ListExtraServicesSerializer,
    ListPaidServicesSerializer,
    RetrieveExtraServicesSerializer,
    RetrievePaidServicesSerializer,
)


@extend_schema(tags=["extra_services"])
class ExtraServicesView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ExtraServicesModel.objects.all()
    serializer_class = ListExtraServicesSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListExtraServicesSerializer,
        "retrieve": RetrieveExtraServicesSerializer,
        "create": CreateExtraServicesSerializer,
    }


@extend_schema(tags=["paid_services"])
class PaidServicesView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PaidServicesModel.objects.all()
    serializer_class = ListPaidServicesSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPaidServicesSerializer,
        "retrieve": RetrievePaidServicesSerializer,
        "create": CreatePaidServicesSerializer,
    }
