from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from core.apps.blog.permissions.post import IsModeratorOrReadOnly
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from core.apps.blog.models import CategoryModel, PostModel, TagModel
from core.apps.blog.serializers import UpdatePostSerializer
from django_filters.rest_framework import DjangoFilterBackend
from core.apps.blog.filters.post import TagFilter, PostFilter
from core.apps.accounts.choices.user import RoleChoice
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
class PostView(BaseViewSetMixin, ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = BaseViewSetMixin
    permission_classes = [IsModeratorOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete']
    filterset_class = PostFilter
    filter_backends = [DjangoFilterBackend]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPostSerializer,
        "retrieve": RetrievePostSerializer,
        "partial_update": UpdatePostSerializer,
        "create": CreatePostSerializer,
    }

    def get_queryset(self):
        qs = PostModel.objects.all()
        user = self.request.user

        if user.is_authenticated and user.role == RoleChoice.Moderator:
            return qs

        return qs.filter(is_public=True)


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
