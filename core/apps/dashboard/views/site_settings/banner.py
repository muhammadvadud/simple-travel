from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet

from core.apps.dashboard.filters.banner import BannerFilter
from core.apps.api.models import BannerModel
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from core.apps.dashboard.permission.general_permission import IsModerator
from core.apps.dashboard.serializers.site_settings import ListBannerSerializer, CreateBannerSerializer, \
    RetrieveBannerSerializer
from rest_framework.response import Response


@extend_schema(tags=["Dashboard-Banner"])
class BannerViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = BannerModel.objects.all().order_by("-id")
    serializer_class = ListBannerSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]
    filter_backends = [DjangoFilterBackend]
    filterset_class = BannerFilter

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListBannerSerializer,
        "retrieve": RetrieveBannerSerializer,
        "create": CreateBannerSerializer,
        "partial_update": RetrieveBannerSerializer,
    }
