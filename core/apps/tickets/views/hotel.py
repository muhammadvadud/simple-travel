from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.tickets.models import HotelModel
from core.apps.tickets.serializers.hotel import CreateHotelSerializer, ListHotelSerializer, RetrieveHotelSerializer


@extend_schema(tags=["hotel"])
class HotelView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = HotelModel.objects.all()
    serializer_class = ListHotelSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListHotelSerializer,
        "retrieve": RetrieveHotelSerializer,
        "create": CreateHotelSerializer,
    }
