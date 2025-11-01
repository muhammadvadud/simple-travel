from rest_framework import serializers
from core.apps.tickets.models import TicketsAmenitiesModel


class BaseTicketsAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsAmenitiesModel
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
            "icon_name",
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
            "icon_name",
        ]


class CreateTicketsAmenitiesSerializer(BaseTicketsAmenitiesSerializer):
    class Meta(BaseTicketsAmenitiesSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
            "icon_name",
        ]
