from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from core.apps.api.models import FaqModel
from drf_spectacular.utils import extend_schema
from ...permission.general_permission import IsModerator
from ...serializers import ListFaqSerializer, CreateFaqSerializer, RetrieveFaqSerializer


@extend_schema(tags=["Dashboard-Faq"])
class FaqViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = FaqModel.objects.all()
    serializer_class = ListFaqSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {}
    action_serializer_class = {
        "list": ListFaqSerializer,
        "retrieve": RetrieveFaqSerializer,
        "create": CreateFaqSerializer,
        "partial_update": RetrieveFaqSerializer,
    }
