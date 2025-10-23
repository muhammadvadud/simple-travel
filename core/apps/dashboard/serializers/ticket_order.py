from rest_framework import serializers
from core.apps.tickets.models import TicketorderModel, ExtraServicesModel, PaidServicesModel
from core.apps.accounts.models import ParticipantModel
from django.contrib.auth import get_user_model

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantModel
        fields = [
            "first_name",
            "last_name",
        ]

class PaidServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidServicesModel
        fields = ["name", "price"]


class ExtraServicesModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraServicesModel
        fields = ["name"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
        ]


class BaseTicketOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    extra_service = ExtraServicesModelSerializer(many=True, read_only=True)
    extra_paid_service = PaidServicesSerializer(many=True, read_only=True)

    class Meta:
        model = TicketorderModel
        fields = [
            "id",
            "user",
            "departure",
            "destination",
            "departure_date",
            "arrival_time",
            "participant",
            "ticket",
            "tariff",
            "transport",
            "extra_service",
            "extra_paid_service",
            "order_status",
            "total_price",
        ]


class ListTicketOrderSerializer(BaseTicketOrderSerializer):
    class Meta(BaseTicketOrderSerializer.Meta): ...


class RetrieveTicketOrderSerializer(BaseTicketOrderSerializer):
    class Meta(BaseTicketOrderSerializer.Meta): ...


class CreateTicketOrderSerializer(BaseTicketOrderSerializer):
    role = serializers.CharField(write_only=True, required=True)

    class Meta(BaseTicketOrderSerializer.Meta):
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "password",
            "role"
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        role_status = validated_data.pop("role", None)
        if not role_status:
            raise serializers.ValidationError("Role status is required")

        password = validated_data.pop("password", None)
        user = get_user_model().objects.create(**validated_data)
        user.role = role_status

        if password:
            user.set_password(password)
            user.save()

        return user
