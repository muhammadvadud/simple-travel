from rest_framework import serializers
from core.apps.tickets.models import Region, Country


class BaseRegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
        ]


class ListRegionSerializer(BaseRegionSerializer):
    class Meta(BaseRegionSerializer.Meta): ...


class RetrieveRegionSerializer(BaseRegionSerializer):
    class Meta(BaseRegionSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
        ]


class CreateRegionSerializer(BaseRegionSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())

    class Meta(BaseRegionSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
            "country",
        ]


class UpdateRegionSerializer(BaseRegionSerializer):
    country = serializers.PrimaryKeyRelatedField(queryset=Country.objects.all())

    class Meta(BaseRegionSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
            "country",
        ]
