from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins

from core.apps.api.models import FaqCategoryModel
from core.apps.api.serializers.faq import CreateFaqSerializer, RetrieveFaqSerializer, \
    FaqCategoryWithFaqsSerializer


@extend_schema(tags=["faq"])
class FaqView(BaseViewSetMixin, mixins.ListModelMixin, GenericViewSet):
    queryset = FaqCategoryModel.objects.all()
    serializer_class = FaqCategoryWithFaqsSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": FaqCategoryWithFaqsSerializer,
    }
