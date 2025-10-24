from rest_framework import serializers
from core.apps.accounts.models import SupportModel


class BaseDashboardSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportModel
        fields = [
            "id",
            "name",
            "phone_number",
            "travel_agency",
        ]


class ListDashboardSupportSerializer(BaseDashboardSupportSerializer):
    class Meta(BaseDashboardSupportSerializer.Meta): ...


class RetrieveDashboardSupportSerializer(BaseDashboardSupportSerializer):
    class Meta(BaseDashboardSupportSerializer.Meta): ...
