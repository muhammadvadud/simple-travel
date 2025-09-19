from rest_framework import serializers

from core.apps.tickets.models import HotelModel


class BaseHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields = [
            "id",
            "name",
        ]


class ListHotelSerializer(BaseHotelSerializer):
    class Meta(BaseHotelSerializer.Meta): ...


class RetrieveHotelSerializer(BaseHotelSerializer):
    class Meta(BaseHotelSerializer.Meta): ...


class CreateHotelSerializer(BaseHotelSerializer):
    class Meta(BaseHotelSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
