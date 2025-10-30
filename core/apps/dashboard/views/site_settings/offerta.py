from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet

from core.apps.dashboard.filters import OffertaFilter
from core.apps.dashboard.models import Offerta
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.accounts.choices import RoleChoice
from core.apps.dashboard.serializers.site_settings import ListOffertaSerializer, CreateOffertaSerializer, \
    RetrieveOffertaSerializer, PublicOffertaSerializer


@extend_schema(tags=["Dashboard-Offerta"])
class OffertaViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = Offerta.objects.all().order_by("-id")
    serializer_class = PublicOffertaSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = OffertaFilter
    action_permission_classes = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
    }

    action_serializer_class = {
        "list": PublicOffertaSerializer,
        "retrieve": PublicOffertaSerializer,
        "create": CreateOffertaSerializer,
        "partial_update": RetrieveOffertaSerializer,
    }

    def get_serializer_class(self):
        action = self.action
        user = self.request.user

        serializer_class = self.action_serializer_class.get(action, self.serializer_class)

        if action == "list":
            if user.is_authenticated and user.role == RoleChoice.Moderator:
                return ListOffertaSerializer
            else:
                return PublicOffertaSerializer
        elif action == "retrieve":
            if user.is_authenticated and user.role == RoleChoice.Moderator:
                return RetrieveOffertaSerializer
            else:
                return PublicOffertaSerializer
        return serializer_class
