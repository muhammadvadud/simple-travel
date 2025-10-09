from django.db.models import QuerySet
from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet
from ..permissions.participant import ParticipantPermission

from core.apps.accounts.models import ParticipantModel
from core.apps.accounts.serializers.participant import (
    CreateParticipantSerializer,
    ListParticipantSerializer,
    RetrieveParticipantSerializer,
)


@extend_schema(tags=["participant"])
class ParticipantView(BaseViewSetMixin, ModelViewSet):
    serializer_class = ListParticipantSerializer
    permission_classes = [ParticipantPermission]
    http_method_names = ["get", "post", "patch", "delete"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListParticipantSerializer,
        "retrieve": RetrieveParticipantSerializer,
        "create": CreateParticipantSerializer,
    }

    def get_queryset(self):
        participant = ParticipantModel.objects.filter(created_by=self.request.user)
        return participant
