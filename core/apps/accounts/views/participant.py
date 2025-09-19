from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.accounts.models import ParticipantModel
from core.apps.accounts.serializers.participant import (
    CreateParticipantSerializer,
    ListParticipantSerializer,
    RetrieveParticipantSerializer,
)


@extend_schema(tags=["participant"])
class ParticipantView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = ParticipantModel.objects.all()
    serializer_class = ListParticipantSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListParticipantSerializer,
        "retrieve": RetrieveParticipantSerializer,
        "create": CreateParticipantSerializer,
    }
