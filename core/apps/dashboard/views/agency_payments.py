from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.dashboard.models import TravelAgencyPaymentModel
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices.user import RoleChoice
from ..permission.general_permission import IsModeratorOrBuxgalter
from ..serializers import ListTravelAgencyPaymentsSerializer, CreateTravelAgencyPaymentsSerializer, \
    RetrieveTravelAgencyPaymentsSerializer, UpdateTravelAgencyPaymentsSerializer


@extend_schema(tags=["Dashboard-TravelAgencyPayments"])
class TravelAgencyPaymentsViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = TravelAgencyPaymentModel.objects.all()
    serializer_class = ListTravelAgencyPaymentsSerializer
    permission_classes = [IsModeratorOrBuxgalter]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTravelAgencyPaymentsSerializer,
        "retrieve": RetrieveTravelAgencyPaymentsSerializer,
        "create": CreateTravelAgencyPaymentsSerializer,
        "partial_update": UpdateTravelAgencyPaymentsSerializer,
    }
