from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.accounts.models import TravelAgency
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices.travel_agency import TravelAgencyStatusChoices
from ..filters.agency_request import TravelAgencyFilter
from ..permission.general_permission import IsModerator
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from ..serializers.agency_request import ListDashboardTravelAgencyRequestSerializer, \
    RetrieveDashboardTravelAgencyRequestSerializer


@extend_schema(tags=["Dashboard-TravelAgency-Request"])
class TravelAgencyRequestViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = TravelAgency.objects.filter(status=TravelAgencyStatusChoices.PENDING)
    serializer_class = ListDashboardTravelAgencyRequestSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "patch", "head", "options"]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['name', 'email', 'phone']
    filterset_class = TravelAgencyFilter
    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDashboardTravelAgencyRequestSerializer,
        "retrieve": RetrieveDashboardTravelAgencyRequestSerializer,
        "partial_update": RetrieveDashboardTravelAgencyRequestSerializer,
    }
