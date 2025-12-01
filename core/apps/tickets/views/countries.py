from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.tickets.models import Country
from core.apps.tickets.serializers.coutries import CreateCountrySerializer, ListCountrySerializer, \
    RetrieveCountrySerializer


@extend_schema(tags=["Country"])
class CountryView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = Country.objects.all()
    serializer_class = ListCountrySerializer
    permission_classes = [AllowAny]
    pagination_class = None
    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCountrySerializer,
        "retrieve": RetrieveCountrySerializer,
        "create": CreateCountrySerializer,
    }
