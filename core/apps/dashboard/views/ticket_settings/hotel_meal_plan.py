from django_core.mixins import BaseViewSetMixin
from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from core.apps.tickets.models import HotelMealPlan
from core.apps.dashboard.permission import IsModerator, IsModeratorOrTourAdminOrOperator
from core.apps.dashboard.serializers.ticket_settings.hotel_meal_plan import (
    ListHotelMealPlanSerializer, RetrieveHotelMealPlanSerializer, CreateHotelMealPlanSerializer
)


@extend_schema(tags=["Ticket Settings Hotel Meal Plan"])
class HotelMealPlanViewSet(BaseViewSetMixin, ModelViewSet):
    queryset = HotelMealPlan.objects.all().order_by("-id")
    serializer_class = ListHotelMealPlanSerializer
    permission_classes = [IsModerator]
    http_method_names = ["get", "post", "patch", "delete", "head", "options"]

    action_permission_classes = {
        "list": [IsModeratorOrTourAdminOrOperator],
        "retrieve": [IsModeratorOrTourAdminOrOperator]
    }
    action_serializer_class = {
        "list": ListHotelMealPlanSerializer,
        "retrieve": RetrieveHotelMealPlanSerializer,
        "create": CreateHotelMealPlanSerializer,
        "partial_update": RetrieveHotelMealPlanSerializer,
    }
