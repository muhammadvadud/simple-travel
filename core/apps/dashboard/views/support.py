from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.accounts.models import SupportModel
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices.user import RoleChoice
from django_filters.rest_framework import DjangoFilterBackend
from ..permission.general_permission import IsModeratorOrTourAdminOrOperator
from ..filters.support import SupportFilter
from ..serializers.support import ListDashboardSupportSerializer, RetrieveDashboardSupportSerializer


@extend_schema(tags=["Dashboard-Support"])
class SupportViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = SupportModel.objects.all()
    serializer_class = ListDashboardSupportSerializer
    permission_classes = [IsModeratorOrTourAdminOrOperator]
    http_method_names = ["get", "patch", "delete", "head", "options"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupportFilter
    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDashboardSupportSerializer,
        "retrieve": RetrieveDashboardSupportSerializer,
        "partial_update": RetrieveDashboardSupportSerializer,
    }

    def get_queryset(self):
        user = self.request.user
        if user.role == RoleChoice.TourAdmin:
            return SupportModel.objects.filter(travel_agency=user.travel_agency)

        elif user.role == RoleChoice.Operator:
            return SupportModel.objects.filter(travel_agency__isnull=True)

        return SupportModel.objects.all()
