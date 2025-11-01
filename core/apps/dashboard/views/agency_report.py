from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ReadOnlyModelViewSet
from core.apps.accounts.models import TravelAgency
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices import RoleChoice
from ..permission.general_permission import IsModeratorOrTourAdminOrBuxgalter
from ..serializers import ListDashboardTravelAgencyReportSerializer, \
    RetrieveDashboardTravelAgencyReportSerializer


@extend_schema(tags=["Dashboard-TravelAgency-Report"])
class TravelAgencyReportViewSet(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TravelAgency.objects.filter(status="approved").order_by("-id")
    serializer_class = ListDashboardTravelAgencyReportSerializer
    permission_classes = [IsModeratorOrTourAdminOrBuxgalter]
    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDashboardTravelAgencyReportSerializer,
        "retrieve": RetrieveDashboardTravelAgencyReportSerializer,
    }

    def get_queryset(self):
        qs = super().get_queryset()
        user = self.request.user
        if user.is_authenticated:
            if user.role == RoleChoice.TourAdmin:
                return qs.filter(id=user.travel_agency.id)

        return qs
