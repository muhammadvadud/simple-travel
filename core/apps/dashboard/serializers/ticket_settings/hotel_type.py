from rest_framework import serializers
from core.apps.tickets.models import HotelTypeModel


class BaseHotelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelTypeModel
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
        ]


class ListHotelTypeSerializer(BaseHotelTypeSerializer):
    class Meta(BaseHotelTypeSerializer.Meta): ...


class RetrieveHotelTypeSerializer(BaseHotelTypeSerializer):
    class Meta(BaseHotelTypeSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
        ]


class CreateHotelTypeSerializer(BaseHotelTypeSerializer):
    class Meta(BaseHotelTypeSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
        ]
