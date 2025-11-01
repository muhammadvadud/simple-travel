from rest_framework import serializers
from core.apps.tickets.models import TicketsAmenitiesModel


class BaseTicketsAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsAmenitiesModel
        fields = [
            "id",
            "name",
            "color",
        ]


class ListTicketsAmenitiesSerializer(BaseTicketsAmenitiesSerializer):
    class Meta(BaseTicketsAmenitiesSerializer.Meta): ...


class RetrieveTicketsAmenitiesSerializer(BaseTicketsAmenitiesSerializer):
    class Meta(BaseTicketsAmenitiesSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
            "color",
        ]


class CreateTicketsAmenitiesSerializer(BaseTicketsAmenitiesSerializer):
    class Meta(BaseTicketsAmenitiesSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
            "color",
        ]
