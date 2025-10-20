from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.apps.tickets.models.tickets import TicketorderModel


class UserOrderSerializer(serializers.ModelSerializer):
    travel_agency_id = serializers.SerializerMethodField()

    class Meta:
        model = TicketorderModel
        fields = [
            "id",
            "departure",
            "destination",
            "ticket",
            "travel_agency_id",
        ]

    def get_travel_agency_id(self, obj):
        travel_id = getattr(obj.ticket.travel_agency, "custom_id", None)
        if travel_id is not None:
            return f"{travel_id}"
        return None


class BaseUsersSerializer(serializers.ModelSerializer):
    orders = UserOrderSerializer(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "phone",
            "email",
            "avatar",
            "validated_at",
            "orders",
        ]


class ListUsersSerializer(BaseUsersSerializer):
    class Meta(BaseUsersSerializer.Meta):
        fields = [
            "id",
            "phone",
            "email",
            "avatar",
            "validated_at",
        ]


class RetrieveUsersSerializer(BaseUsersSerializer):
    class Meta(BaseUsersSerializer.Meta): ...
