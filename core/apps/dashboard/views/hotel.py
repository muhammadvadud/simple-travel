from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.tickets.models import HotelModel
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices.user import RoleChoice
from django_filters.rest_framework import DjangoFilterBackend
from ..filters.hotel import HotelFilter
from ..permission.tickets import IsModeratorOrTourAdmin
from ..serializers.hotel import RetrieveHotelSerializer, CreateHotelSerializer, ListHotelSerializer


@extend_schema(tags=["Dashboard-Hotel"])
class HotelViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = HotelModel.objects.all().order_by("-id")
    serializer_class = CreateHotelSerializer
    permission_classes = [IsModeratorOrTourAdmin]
    http_method_names = ["get", "post", "patch", "head", "options"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = HotelFilter
    action_permission_classes = {}
    action_serializer_class = {
        "list": ListHotelSerializer,
        "retrieve": RetrieveHotelSerializer,
        "create": CreateHotelSerializer,
        "partial_update": CreateHotelSerializer,
    }

    def get_queryset(self):
        user = self.request.user
        if user.role == RoleChoice.TourAdmin:
            return HotelModel.objects.filter(ticket__travel_agency_id=user.travel_agency.id)
        else:
            return HotelModel.objects.all()
