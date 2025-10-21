from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from core.apps.accounts.models.travel_agency import TravelAgency
from ..serializers.tour_agency import FullListTravelAgencySerializer, RetrieveTravelAgencySerializer, \
    BaseTravelAgencySerializer
from ..permission.tour_agency import IsModerator, IsOperatorOrModerator


@extend_schema(tags=["Dashboard-TourAgency"])
class TourAgencyViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = TravelAgency.objects.all()
    serializer_class = FullListTravelAgencySerializer
    permission_classes = [IsOperatorOrModerator]
    http_method_names = ['get', 'patch', 'delete', 'head', 'options']

    action_permission_classes = {
        "partial_update": [IsModerator],
    }
    action_serializer_class = {
        "list": FullListTravelAgencySerializer,
        "retrieve": RetrieveTravelAgencySerializer,
        "partial_update": RetrieveTravelAgencySerializer
    }

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        pagination_queryset = self.paginate_queryset(queryset)
        serializer = FullListTravelAgencySerializer({"list": pagination_queryset})
        response = self.get_paginated_response(serializer.data)
        return response
