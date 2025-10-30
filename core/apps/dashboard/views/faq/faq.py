from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.api.models import FaqModel
from drf_spectacular.utils import extend_schema

from ...filters.faq import FaqFilter
from ...permission.general_permission import IsModerator
from ...serializers import ListFaqSerializer, CreateFaqSerializer, RetrieveFaqSerializer
from django_filters.rest_framework import DjangoFilterBackend


@extend_schema(tags=["Dashboard-Faq"])
class FaqViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = FaqModel.objects.all().order_by("-id")
    serializer_class = ListFaqSerializer
    permission_classes = [IsModerator]
    filter_backends = [DjangoFilterBackend]
    filterset_class = FaqFilter
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListFaqSerializer,
        "retrieve": RetrieveFaqSerializer,
        "create": CreateFaqSerializer,
        "partial_update": RetrieveFaqSerializer,
    }
