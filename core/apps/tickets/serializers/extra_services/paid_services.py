from rest_framework import serializers

from core.apps.tickets.models import PaidServicesModel


class BasePaidServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidServicesModel
        fields = [
            "id",
            "name",
        ]


class ListPaidServicesSerializer(BasePaidServicesSerializer):
    class Meta(BasePaidServicesSerializer.Meta): ...


class RetrievePaidServicesSerializer(BasePaidServicesSerializer):
    class Meta(BasePaidServicesSerializer.Meta): ...


class CreatePaidServicesSerializer(BasePaidServicesSerializer):
    class Meta(BasePaidServicesSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
