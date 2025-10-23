from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.accounts.models import SupportModel
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices.user import RoleChoice
from ..permission.general_permission import IsModeratorOrTourAdminOrOperator
from ..serializers.support import ListSupportSerializer, RetrieveSupportSerializer


@extend_schema(tags=["Dashboard-Support"])
class SupportViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = SupportModel.objects.all()
    serializer_class = ListSupportSerializer
    permission_classes = [IsModeratorOrTourAdminOrOperator]
    http_method_names = ["get", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListSupportSerializer,
        "retrieve": RetrieveSupportSerializer,
        "partial_update": RetrieveSupportSerializer,
    }

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated and user.role == RoleChoice.TourAdmin:
            queryset = SupportModel.objects.filter(travel_agency=user.travel_agency)
            return queryset
        elif user.is_authenticated and user.role == RoleChoice.Operator:
            queryset = SupportModel.objects.filter(travel_agency=user.travel_agency)
        else:
            queryset = SupportModel.objects.all()

        return queryset
