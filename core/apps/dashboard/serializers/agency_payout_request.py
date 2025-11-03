from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.apps.accounts.models import TravelAgency

from core.apps.dashboard.models import AgencyPayoutRequestModel


class BaseTravelAgencyPayOutRequestSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = AgencyPayoutRequestModel
        fields = [
            "id",
            "travel_agency",
            "amount",
            "status",
            "created_at",
        ]


class ListTravelAgencyPayOutRequestSerializer(BaseTravelAgencyPayOutRequestSerializer):
    class Meta(BaseTravelAgencyPayOutRequestSerializer.Meta): ...


class RetrieveTravelAgencyPayOutRequestSerializer(BaseTravelAgencyPayOutRequestSerializer):
    class Meta(BaseTravelAgencyPayOutRequestSerializer.Meta): ...


class CreateTravelAgencyPayOutRequestSerializer(BaseTravelAgencyPayOutRequestSerializer):
    class Meta(BaseTravelAgencyPayOutRequestSerializer.Meta):
        fields = [
            "amount",
        ]

    def create(self, validated_data):
        validated_data['travel_agency'] = self.context['request'].user.travel_agency
        if not validated_data['travel_agency']:
            raise ValidationError("You are not Travel Agency Admin")
        request = AgencyPayoutRequestModel.objects.create(**validated_data)
        return request


class UpdateTravelAgencyPayOutRequestSerializer(BaseTravelAgencyPayOutRequestSerializer):
    class Meta(BaseTravelAgencyPayOutRequestSerializer.Meta):
        fields = [
            "status",
        ]
