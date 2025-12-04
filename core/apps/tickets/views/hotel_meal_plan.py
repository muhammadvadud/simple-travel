from django_core.mixins import BaseViewSetMixin
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from core.apps.tickets.models import HotelMealPlan
from core.apps.tickets.serializers.hotel.hotel_meal_plan import CreateHotelMealPlanSerializer, \
    ListHotelMealPlanSerializer, RetrieveHotelMealPlanSerializer


@extend_schema(tags=["HotelMealPlan"])
class HotelMealPlanView(BaseViewSetMixin, ReadOnlyModelViewSet):
    queryset = HotelMealPlan.objects.all()
    serializer_class = ListHotelMealPlanSerializer
    permission_classes = [AllowAny]
    pagination_class = None
    action_permission_classes = {}
    action_serializer_class = {
        "list": ListHotelMealPlanSerializer,
        "retrieve": RetrieveHotelMealPlanSerializer,
        "create": CreateHotelMealPlanSerializer,
    }
