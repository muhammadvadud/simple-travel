from rest_framework import serializers
from core.apps.tickets.models import TariffModel


class BaseDashboardTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffModel
        fields = [
            "id",
            "name",
        ]


class ListDashboardTariffSerializer(BaseDashboardTariffSerializer):
    class Meta(BaseDashboardTariffSerializer.Meta):
        ref_name = "ListDashboardTariff"


class RetrieveDashboardTariffSerializer(BaseDashboardTariffSerializer):
    class Meta(BaseDashboardTariffSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
        ]
        ref_name = "RetrieveDashboardTariff"


class CreateDashboardTariffSerializer(BaseDashboardTariffSerializer):
    class Meta(BaseDashboardTariffSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
        ]
