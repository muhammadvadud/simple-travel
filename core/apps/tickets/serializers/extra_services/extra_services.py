from rest_framework import serializers

from core.apps.tickets.models import ExtraServicesModel


class BaseExtraServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraServicesModel
        fields = [
            "id",
            "name",
        ]


class ListExtraServicesSerializer(BaseExtraServicesSerializer):
    class Meta(BaseExtraServicesSerializer.Meta): ...


class RetrieveExtraServicesSerializer(BaseExtraServicesSerializer):
    class Meta(BaseExtraServicesSerializer.Meta): ...


class CreateExtraServicesSerializer(BaseExtraServicesSerializer):
    class Meta(BaseExtraServicesSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
