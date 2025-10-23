from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from core.apps.accounts.choices.user import RoleChoice
from ..permission.tickets import IsModeratorOrTourAdmin
from ..serializers.hotel import RetrieveHotelSerializer, CreateHotelSerializer


@extend_schema(tags=["Dashboard-Hotel"])
class HotelViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = get_user_model().objects.filter(role__in=[RoleChoice.Buxgalter, RoleChoice.Operator])
    serializer_class = CreateHotelSerializer
    permission_classes = [IsModeratorOrTourAdmin]
    http_method_names = ["post", "patch", "head", "options"]

    action_permission_classes = {

    }
    action_serializer_class = {
        "create": CreateHotelSerializer,
        "partial_update": RetrieveHotelSerializer,
    }
