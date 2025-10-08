from rest_framework import serializers

from core.apps.accounts.models import SupportModel
from core.apps.accounts.models import TravelAgency


class BaseSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportModel
        fields = [
            "id",
            "name",
        ]


class ListSupportSerializer(BaseSupportSerializer):
    class Meta(BaseSupportSerializer.Meta): ...


class RetrieveSupportSerializer(BaseSupportSerializer):
    class Meta(BaseSupportSerializer.Meta): ...


class CreateSupportSerializer(BaseSupportSerializer):
    travel_agency = serializers.PrimaryKeyRelatedField(
        queryset=TravelAgency.objects.all(),
        required=False,
        allow_null=True
    )

    class Meta(BaseSupportSerializer.Meta):
        fields = [
            "name",
            "phone_number",
            "travel_agency",
        ]
