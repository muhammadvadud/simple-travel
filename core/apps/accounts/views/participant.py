from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..permissions.participant import ParticipantPermission
from rest_framework.exceptions import PermissionDenied, NotFound
from core.apps.accounts.models import ParticipantModel,ParticipantPasportImageModel
from rest_framework.response import Response
from core.apps.accounts.serializers.participant import (
    CreateParticipantSerializer,
    ListParticipantSerializer,
    RetrieveParticipantSerializer,
    UpdateParticipantSerializer,
    ParticipantPasportImageDestroySerializer,
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
        "partial_update": UpdateParticipantSerializer,
    }

    def get_queryset(self):
        participant = ParticipantModel.objects.filter(created_by=self.request.user)
        return participant


@extend_schema(tags=["participant"])
class ParticipantPasportImageView(ModelViewSet):
    queryset = ParticipantPasportImageModel.objects.all()
    serializer_class = ParticipantPasportImageDestroySerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ["delete"]

    def destroy(self, request, *args, **kwargs):
        image = self.get_object()

        if image.participant.created_by != request.user:
            raise PermissionDenied("Siz faqat o‘zingizga tegishli rasmlarni o‘chira olasiz.")

        image.delete()
        return Response({"status": True, "message": "Rasm o‘chirildi"}, status=204)
