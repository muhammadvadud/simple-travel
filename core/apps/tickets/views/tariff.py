from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.tickets.models import TariffModel
from core.apps.tickets.serializers.tariff import CreateTariffSerializer, ListTariffSerializer, RetrieveTariffSerializer


@extend_schema(tags=["tariff"])
class TariffView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TariffModel.objects.all()
    serializer_class = ListTariffSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTariffSerializer,
        "retrieve": RetrieveTariffSerializer,
        "create": CreateTariffSerializer,
    }
