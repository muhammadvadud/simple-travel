from rest_framework import serializers
from core.apps.accounts.models.travel_agency import TravelAgency
from ..models import TravelAgencyPaymentModel
from django.contrib.auth import get_user_model


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "role"
        ]


class TravelAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelAgency
        fields = [
            "custom_id",
            "name",
            "email",
            "phone",
        ]


class BaseTravelAgencyPaymentsSerializer(serializers.ModelSerializer):
    travel_agency = TravelAgencySerializer(read_only=True)
    accountant = UserInfoSerializer(read_only=True)

    class Meta:
        model = TravelAgencyPaymentModel
        fields = [
            "id",
            "travel_agency",
            "amount",
            "note",
            "accountant",
        ]


class ListTravelAgencyPaymentsSerializer(BaseTravelAgencyPaymentsSerializer):
    class Meta(BaseTravelAgencyPaymentsSerializer.Meta): ...


class RetrieveTravelAgencyPaymentsSerializer(BaseTravelAgencyPaymentsSerializer):
    class Meta(BaseTravelAgencyPaymentsSerializer.Meta): ...


class CreateTravelAgencyPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelAgencyPaymentModel
        fields = [
            "id",
            "travel_agency",
            "amount",
            "note",
        ]

    def create(self, validated_data):
        validated_data['accountant'] = self.context['request'].user
        travel_agency = TravelAgencyPaymentModel.objects.create(**validated_data)
        return travel_agency


class UpdateTravelAgencyPaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelAgencyPaymentModel
        fields = [
            "id",
            "travel_agency",
            "amount",
            "note",
        ]

    def update(self, instance, validated_data):
        instance.accountant = self.context["request"].user

        travel_agency = validated_data.pop("travel_agency", None)
        if travel_agency is not None:
            instance.travel_agency = travel_agency

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance
