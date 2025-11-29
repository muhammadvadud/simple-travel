from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from django_core.mixins.base import BaseViewSetMixin
from rest_framework import status, mixins
from core.apps.api.serializers import LocationListSerializer
from core.services.locations import get_locations_by_language
from drf_spectacular.utils import extend_schema


@extend_schema(tags=["Locations"])
class LocationViewSet(BaseViewSetMixin, mixins.ListModelMixin, GenericViewSet):
    serializer_class = LocationListSerializer
    permission_classes = [AllowAny]

    def list(self, request, *args, **kwargs):
        data = get_locations_by_language(request.LANGUAGE_CODE)
        serializer = self.get_serializer(data)
        ser_data = serializer.data
        return Response(ser_data, status=status.HTTP_200_OK)
