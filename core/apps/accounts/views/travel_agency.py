from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework import mixins

from core.apps.accounts.models import TravelAgency
from core.apps.accounts.serializers.tour_agency.travel_agency import (
    CreateTravelAgencySerializer,
    ListTravelAgencySerializer,
    RetrieveTravelAgencySerializer,
)


@extend_schema(tags=["Travel Agency"])
class TravelAgencyView(BaseViewSetMixin,mixins.CreateModelMixin, GenericViewSet):
    queryset = TravelAgency.objects.all()
    serializer_class = ListTravelAgencySerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTravelAgencySerializer,
        "retrieve": RetrieveTravelAgencySerializer,
        "create": CreateTravelAgencySerializer,
    }
