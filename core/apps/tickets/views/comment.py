from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from ..permissions.comment import IsTicketBuyer
from core.apps.tickets.models import TicketsCommentsModel
from core.apps.tickets.serializers.comment import CreateTicketComment


@extend_schema(tags=["comment"])
class TicketsCommentsViewSet(BaseViewSetMixin, mixins.CreateModelMixin, GenericViewSet):
    queryset = TicketsCommentsModel.objects.all()
    serializer_class = CreateTicketComment
    permission_classes = [IsTicketBuyer]

