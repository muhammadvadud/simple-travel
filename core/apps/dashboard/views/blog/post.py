from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from core.apps.blog.permissions.post import IsModeratorOrReadOnly
from rest_framework.viewsets import ModelViewSet
from core.apps.blog.models import PostModel
from core.apps.accounts.choices.user import RoleChoice
from drf_nested_forms.parsers import NestedMultiPartParser
from rest_framework.parsers import FormParser, MultiPartParser
from core.apps.dashboard.serializers.blog.post import (
    ListDashboardPostSerializer,
    RetrieveDashboardPostSerializer,
    UpdateDashboardPostSerializer,
    CreateDashboardPostSerializer,
)


@extend_schema(tags=["Dashboard-Post"])
class PostView(BaseViewSetMixin, ModelViewSet):
    queryset = PostModel.objects.all().order_by("-id")
    serializer_class = ListDashboardPostSerializer
    permission_classes = [IsModeratorOrReadOnly]
    http_method_names = ['get', 'post', 'patch', 'delete', 'head', 'options']
    parser_classes = [
        NestedMultiPartParser,
        FormParser,
        MultiPartParser,
    ]
    action_permission_classes = {}
    action_serializer_class = {
        "list": ListDashboardPostSerializer,
        "retrieve": RetrieveDashboardPostSerializer,
        "create": CreateDashboardPostSerializer,
        "partial_update": UpdateDashboardPostSerializer,
    }

    def get_queryset(self):
        qs = PostModel.objects.all()
        user = self.request.user

        if user.is_authenticated and user.role == RoleChoice.Moderator:
            return qs

        return qs.filter(is_public=True)

    def partial_update(self, request, *args, **kwargs):
        print("REQ DATA:", request.data)
        return super().partial_update(request, *args, **kwargs)
