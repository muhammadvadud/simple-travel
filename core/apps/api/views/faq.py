from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.response import Response

from core.apps.api.models import FaqCategoryModel
from core.apps.api.serializers.faq import CreateFaqSerializer, RetrieveFaqSerializer, \
    FaqCategoryWithFaqsSerializer


@extend_schema(tags=["faq"])
class FaqView(mixins.ListModelMixin, GenericViewSet):
    queryset = FaqCategoryModel.objects.all()
    serializer_class = FaqCategoryWithFaqsSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": FaqCategoryWithFaqsSerializer,
    }
    def list(self, request, *args, **kwargs):
        queryset = FaqCategoryModel.objects.all()
        serializer = FaqCategoryWithFaqsSerializer(queryset, many=True)
        return Response(serializer.data)