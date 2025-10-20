from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from core.apps.accounts.models.travel_agency import TravelAgency
from ..serializers.tour_agency import ListTravelAgencySerializer, RetrieveTravelAgencySerializer, \
    CreateTravelAgencySerializer
from ..permission.tour_agency import IsModerator, IsOperatorOrModerator


@extend_schema(tags=["Dashboard-TourAgency"])
class TourAgencyViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = TravelAgency.objects.all()
    serializer_class = ListTravelAgencySerializer
    permission_classes = [IsOperatorOrModerator]
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']

    action_permission_classes = {
        "create": [IsModerator],
        "partial_update": [IsModerator],
    }
    action_serializer_class = {
        "list": ListTravelAgencySerializer,
        "retrieve": RetrieveTravelAgencySerializer,
        "create": CreateTravelAgencySerializer,
    }
