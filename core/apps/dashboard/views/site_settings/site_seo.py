from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.dashboard.models import SiteSeo
from drf_spectacular.utils import extend_schema
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.dashboard.serializers.site_settings import ListSiteSeoSerializer, CreateSiteSeoSerializer, \
    RetrieveSiteSeoSerializer


@extend_schema(tags=["Dashboard-SiteSeo"])
class SiteSeoViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = SiteSeo.objects.all()
    serializer_class = ListSiteSeoSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListSiteSeoSerializer,
        "retrieve": RetrieveSiteSeoSerializer,
        "create": CreateSiteSeoSerializer,
        "partial_update": RetrieveSiteSeoSerializer,
    }
