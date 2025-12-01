from rest_framework import serializers
from core.apps.tickets.models import Country


class BaseCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
        ]


class ListCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta): ...


class RetrieveCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
        ]


class CreateCountrySerializer(BaseCountrySerializer):
    class Meta(BaseCountrySerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
        ]
