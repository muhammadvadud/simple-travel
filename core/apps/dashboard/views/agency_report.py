from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ReadOnlyModelViewSet
from core.apps.accounts.models import TravelAgency
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices import RoleChoice
from ..permission.general_permission import IsModeratorOrBuxgalter
from ..serializers import ListDashboardTravelAgencyReportSerializer, \
    RetrieveDashboardTravelAgencyReportSerializer


@extend_schema(tags=["Dashboard-TravelAgency-Report"])
class TravelAgencyReportViewSet(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TravelAgency.objects.filter(status="approved").order_by("-id")
    serializer_class = ListDashboardTravelAgencyReportSerializer
    permission_classes = [IsModeratorOrBuxgalter]
    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDashboardTravelAgencyReportSerializer,
        "retrieve": RetrieveDashboardTravelAgencyReportSerializer,
    }
