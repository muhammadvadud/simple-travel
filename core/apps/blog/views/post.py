from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.blog.models import CategoryModel, PostModel, TagModel
from core.apps.blog.serializers.post import (
    CreateCategorySerializer,
    CreatePostSerializer,
    CreateTagSerializer,
    ListCategorySerializer,
    ListPostSerializer,
    ListTagSerializer,
    RetrieveCategorySerializer,
    RetrievePostSerializer,
    RetrieveTagSerializer,
)


@extend_schema(tags=["post"])
class PostView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = ListPostSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPostSerializer,
        "retrieve": RetrievePostSerializer,
        "create": CreatePostSerializer,
    }


@extend_schema(tags=["tag"])
class TagView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = TagModel.objects.all()
    serializer_class = ListTagSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListTagSerializer,
        "retrieve": RetrieveTagSerializer,
        "create": CreateTagSerializer,
    }


@extend_schema(tags=["category"])
class CategoryView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.all()
    serializer_class = ListCategorySerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListCategorySerializer,
        "retrieve": RetrieveCategorySerializer,
        "create": CreateCategorySerializer,
    }
