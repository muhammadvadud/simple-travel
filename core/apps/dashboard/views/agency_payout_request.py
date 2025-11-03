from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.dashboard.models import AgencyPayoutRequestModel
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from ..filters.agency_payout_request import AgencyPayoutRequestFilter
from core.apps.accounts.choices.user import RoleChoice
from ..permission.general_permission import IsModeratorOrTourAdminOrBuxgalter, IsTourAdmin
from ..serializers.agency_payout_request import ListTravelAgencyPayOutRequestSerializer, \
    CreateTravelAgencyPayOutRequestSerializer, RetrieveTravelAgencyPayOutRequestSerializer, \
    UpdateTravelAgencyPayOutRequestSerializer


@extend_schema(tags=["Dashboard-TravelAgencyPayOutRequest"])
class TravelAgencyPayOutRequestViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = AgencyPayoutRequestModel.objects.all()
    serializer_class = ListTravelAgencyPayOutRequestSerializer
    permission_classes = [IsModeratorOrTourAdminOrBuxgalter]
    http_method_names = ["get", "post", "patch", "head", "options"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = AgencyPayoutRequestFilter
    action_permission_classes = {
        "create": [IsTourAdmin],
    }
    action_serializer_class = {
        "list": ListTravelAgencyPayOutRequestSerializer,
        "retrieve": RetrieveTravelAgencyPayOutRequestSerializer,
        "create": CreateTravelAgencyPayOutRequestSerializer,
        "partial_update": UpdateTravelAgencyPayOutRequestSerializer,
    }

    def get_queryset(self):
        user = self.request.user
        if user.role == RoleChoice.TourAdmin:
            return AgencyPayoutRequestModel.objects.filter(travel_agency=user.travel_agency)
        else:
            return AgencyPayoutRequestModel.objects.all()
