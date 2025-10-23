from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.blog.models import CategoryModel
from drf_spectacular.utils import extend_schema
from ...permission.general_permission import IsModerator
from ...serializers import ListCategorySerializer, CreateCategorySerializer, RetrieveCategorySerializer


@extend_schema(tags=["Dashboard-Category"])
class CategoryViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = ListCategorySerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCategorySerializer,
        "retrieve": RetrieveCategorySerializer,
        "create": CreateCategorySerializer,
        "partial_update": RetrieveCategorySerializer,
    }
