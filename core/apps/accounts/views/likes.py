from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet, GenericViewSet
from rest_framework import mixins

from core.apps.accounts.models import LikesModel
from core.apps.accounts.serializers.likes import CreateLikesSerializer, ListLikesSerializer, RetrieveLikesSerializer, \
    BaseLikesSerializer


@extend_schema(tags=["likes"])
class LikesView(BaseViewSetMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = LikesModel.objects.all()
    serializer_class = CreateLikesSerializer
    permission_classes = [IsAuthenticated]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListLikesSerializer,
        "retrieve": RetrieveLikesSerializer,
        "create": CreateLikesSerializer,
    }
