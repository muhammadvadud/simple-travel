from rest_framework import serializers

from core.apps.tickets.models import HotelMealPlan


class BaseHotelMealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelMealPlan
        fields = [
            "id",
            "name",
        ]


class ListHotelMealPlanSerializer(BaseHotelMealPlanSerializer):
    class Meta(BaseHotelMealPlanSerializer.Meta): ...


class RetrieveHotelMealPlanSerializer(BaseHotelMealPlanSerializer):
    class Meta(BaseHotelMealPlanSerializer.Meta): ...


class CreateHotelMealPlanSerializer(BaseHotelMealPlanSerializer):
    class Meta(BaseHotelMealPlanSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
