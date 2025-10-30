from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.dashboard.models import SiteSeo
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from core.apps.accounts.choices import RoleChoice
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.dashboard.serializers.site_settings import ListSiteSeoSerializer, CreateSiteSeoSerializer, \
    RetrieveSiteSeoSerializer, PublicSiteSeoSerializer


@extend_schema(tags=["Dashboard-SiteSeo"])
class SiteSeoViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = SiteSeo.objects.all().order_by("-id")
    serializer_class = PublicSiteSeoSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
    }
    action_serializer_class = {
        "list": PublicSiteSeoSerializer,
        "retrieve": PublicSiteSeoSerializer,
        "create": CreateSiteSeoSerializer,
        "partial_update": RetrieveSiteSeoSerializer,
    }

    def get_serializer_class(self):
        action = self.action
        user = self.request.user

        serializer_class = self.action_serializer_class.get(action, self.serializer_class)

        if action == "list":
            if user.is_authenticated and user.role == RoleChoice.Moderator:
                return ListSiteSeoSerializer
            else:
                return PublicSiteSeoSerializer
        elif action == "retrieve":
            if user.is_authenticated and user.role == RoleChoice.Moderator:
                return RetrieveSiteSeoSerializer
            else:
                return PublicSiteSeoSerializer
        return serializer_class
