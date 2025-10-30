from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.dashboard.models import HelpPage
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.dashboard.serializers.site_settings import ListHelpPageSerializer, CreateHelpPageSerializer, \
    RetrieveHelpPageSerializer


@extend_schema(tags=["Dashboard-HelpPage"])
class HelpPageViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = HelpPage.objects.all().order_by("-id")
    serializer_class = ListHelpPageSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
    }
    action_serializer_class = {
        "list": ListHelpPageSerializer,
        "retrieve": RetrieveHelpPageSerializer,
        "create": CreateHelpPageSerializer,
        "partial_update": RetrieveHelpPageSerializer,
    }
