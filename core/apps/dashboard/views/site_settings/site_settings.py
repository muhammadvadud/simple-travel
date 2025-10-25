from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.dashboard.models import SiteSettings
from drf_spectacular.utils import extend_schema
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.dashboard.serializers.site_settings import ListSiteSettingsSerializer, CreateSiteSettingsSerializer, \
    RetrieveSiteSettingsSerializer


@extend_schema(tags=["Dashboard-SiteSettings"])
class SiteSettingsViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = SiteSettings.objects.all()
    serializer_class = ListSiteSettingsSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListSiteSettingsSerializer,
        "retrieve": RetrieveSiteSettingsSerializer,
        "create": CreateSiteSettingsSerializer,
        "partial_update": RetrieveSiteSettingsSerializer,
    }
