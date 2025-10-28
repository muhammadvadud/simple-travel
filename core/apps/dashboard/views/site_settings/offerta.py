from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.dashboard.models import Offerta
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.dashboard.serializers.site_settings import ListOffertaSerializer, CreateOffertaSerializer, \
    RetrieveOffertaSerializer


@extend_schema(tags=["Dashboard-Offerta"])
class OffertaViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = Offerta.objects.all()
    serializer_class = ListOffertaSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
    }

    action_serializer_class = {
        "list": ListOffertaSerializer,
        "retrieve": RetrieveOffertaSerializer,
        "create": CreateOffertaSerializer,
        "partial_update": RetrieveOffertaSerializer,
    }
