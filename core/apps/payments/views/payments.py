from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.payments.models import PaymentsModel
from core.apps.payments.serializers.payments import (
    CreatePaymentsSerializer,
    ListPaymentsSerializer,
    RetrievePaymentsSerializer,
)


@extend_schema(tags=["payments"])
class PaymentsView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = PaymentsModel.objects.all()
    serializer_class = ListPaymentsSerializer
    permission_classes = [AllowAny]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListPaymentsSerializer,
        "retrieve": RetrievePaymentsSerializer,
        "create": CreatePaymentsSerializer,
    }
