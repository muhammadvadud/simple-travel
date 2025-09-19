from rest_framework import serializers

from core.apps.tickets.models import TariffModel


class BaseTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffModel
        fields = [
            "id",
            "name",
        ]


class ListTariffSerializer(BaseTariffSerializer):
    class Meta(BaseTariffSerializer.Meta): ...


class RetrieveTariffSerializer(BaseTariffSerializer):
    class Meta(BaseTariffSerializer.Meta): ...


class CreateTariffSerializer(BaseTariffSerializer):
    class Meta(BaseTariffSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
