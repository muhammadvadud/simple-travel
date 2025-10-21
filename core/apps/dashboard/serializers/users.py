from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.apps.tickets.models.tickets import TicketorderModel
from core.apps.accounts.models.participant import ParticipantModel
from core.apps.tickets.serializers import ListExtraServicesSerializer, ListPaidServicesSerializer
from core.apps.accounts.serializers.participant.participant import RetrieveParticipantSerializer
from django.db.models import Q
from core.apps.accounts.choices.user import RoleChoice


class OrderParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantModel
        fields = [
            "first_name",
            "last_name",
        ]


class UserOrderSerializer(serializers.ModelSerializer):
    travel_agency_id = serializers.SerializerMethodField()
    location_name = serializers.SerializerMethodField()
    participant = OrderParticipantSerializer(many=True, read_only=True)
    extra_service = ListExtraServicesSerializer(many=True, read_only=True)
    extra_paid_service = ListPaidServicesSerializer(many=True, read_only=True)

    class Meta:
        model = TicketorderModel
        fields = [
            "id",
            "departure",
            "destination",
            "ticket",
            "travel_agency_id",
            "tariff",
            "departure_date",
            "arrival_time",
            "location_name",
            "participant",
            "extra_service",
            "extra_paid_service",
            "total_price",
            "order_status",
        ]

    def get_travel_agency_id(self, obj):
        travel_id = getattr(obj.ticket.travel_agency, "custom_id", None)
        if travel_id is not None:
            return f"{travel_id}"
        return None

    def get_location_name(self, obj):
        location_name = obj.ticket.location_name
        if location_name is not None:
            return location_name
        return None


class BaseUsersSerializer(serializers.ModelSerializer):
    orders = UserOrderSerializer(many=True, read_only=True)
    validated_at = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)
    participant = RetrieveParticipantSerializer(many=True, read_only=True)
    ticket_count = serializers.SerializerMethodField()
    participant_count = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "phone",
            "email",
            "avatar",
            "validated_at",
            "orders",
            "participant",
            "ticket_count",
            "participant_count",
        ]

    def get_ticket_count(self, obj):
        return obj.orders.count()

    def get_participant_count(self, obj):
        return obj.participant.count()


class ListUsersSerializer(BaseUsersSerializer):
    class Meta(BaseUsersSerializer.Meta):
        fields = [
            "id",
            "phone",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "validated_at",
        ]


class FullInfoUsersList(serializers.Serializer):
    users = ListUsersSerializer(many=True, read_only=True)
    user_register_phone = serializers.SerializerMethodField(read_only=True)
    user_register_email = serializers.SerializerMethodField(read_only=True)

    def get_user_register_phone(self, obj):
        User = get_user_model()
        count = User.objects.filter(
            Q(role=RoleChoice.USER) & Q(phone__isnull=False) & ~Q(phone="")
        ).count()
        return count

    def get_user_register_email(self, obj):
        User = get_user_model()
        count = User.objects.filter(
            Q(role=RoleChoice.USER) & Q(email__isnull=False) & ~Q(email="")
        ).count()
        return count


class RetrieveUsersSerializer(BaseUsersSerializer):
    class Meta(BaseUsersSerializer.Meta): ...
