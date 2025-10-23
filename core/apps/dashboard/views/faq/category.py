from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.api.models.faq import FaqCategoryModel
from drf_spectacular.utils import extend_schema
from ...permission.general_permission import IsModerator
from ...serializers import ListFaqCategorySerializer, RetrieveFaqCategorySerializer, CreateFaqCategorySerializer


@extend_schema(tags=["Dashboard-FaqCategory"])
class FaqCategoryViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = FaqCategoryModel.objects.all()
    serializer_class = ListFaqCategorySerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListFaqCategorySerializer,
        "retrieve": RetrieveFaqCategorySerializer,
        "create": CreateFaqCategorySerializer,
        "partial_update": RetrieveFaqCategorySerializer,
    }
