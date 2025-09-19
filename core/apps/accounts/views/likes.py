from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.accounts.models import LikesModel
from core.apps.accounts.serializers.likes import CreateLikesSerializer, ListLikesSerializer, RetrieveLikesSerializer


@extend_schema(tags=["likes"])
class LikesView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = LikesModel.objects.all()
    serializer_class = ListLikesSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListLikesSerializer,
        "retrieve": RetrieveLikesSerializer,
        "create": CreateLikesSerializer,
    }
