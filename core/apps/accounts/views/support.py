from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.accounts.models import SupportModel
from core.apps.accounts.serializers.support import (
    CreateSupportSerializer,
    ListSupportSerializer,
    RetrieveSupportSerializer,
)


@extend_schema(tags=["support"])
class SupportView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = SupportModel.objects.all()
    serializer_class = ListSupportSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListSupportSerializer,
        "retrieve": RetrieveSupportSerializer,
        "create": CreateSupportSerializer,
    }
