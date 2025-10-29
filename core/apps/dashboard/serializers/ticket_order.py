from rest_framework import serializers
from core.apps.tickets.models import TicketorderModel, ExtraServicesModel, PaidServicesModel
from core.apps.accounts.models import ParticipantModel, ParticipantPasportImageModel
from django.contrib.auth import get_user_model


class ParticipantPasportImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ParticipantPasportImageModel
        fields = ['image']


class ParticipantSerializer(serializers.ModelSerializer):
    participant_pasport_image = ParticipantPasportImageSerializer(many=True, read_only=True)

    class Meta:
        model = ParticipantModel
        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "phone_number",
            "gender",
            "participant_pasport_image",
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
            "phone",
            "email",
            "validated_at",
            "total_spent",
        ]


class UserListSerializer(serializers.ModelSerializer):
    contact = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "contact",
        ]

    def get_contact(self, obj):
        phone_number = obj.phone
        email = obj.email
        if phone_number:
            return phone_number
        else:
            return email


class BaseTicketOrderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    extra_service = ExtraServicesModelSerializer(many=True, read_only=True)
    extra_paid_service = PaidServicesSerializer(many=True, read_only=True)
    participant = ParticipantSerializer(many=True, read_only=True)

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
    user = UserListSerializer(read_only=True)
    tour_name = serializers.SerializerMethodField()
    tour_id = serializers.SerializerMethodField()

    class Meta(BaseTicketOrderSerializer.Meta):
        fields = [
            "id",
            "user",
            "destination",
            "total_price",
            "order_status",
            "tour_name",
            "tour_id",
        ]

    def get_tour_name(self, obj):
        tour_name = obj.ticket.travel_agency.name
        return tour_name

    def get_tour_id(self, obj):
        tour_id = obj.ticket.travel_agency.id
        return tour_id


class FullTicketOrderSerializer(serializers.Serializer):
    orders = ListTicketOrderSerializer(many=True, read_only=True)
    total_income = serializers.SerializerMethodField()

    def get_total_income(self, obj):
        if isinstance(obj, dict) and "orders" in obj:
            queryset = obj["orders"]
        else:
            queryset = obj

        seen_agencies = set()
        total_income = 0

        for order in queryset:
            try:
                agency = order.ticket.travel_agency
            except AttributeError:
                continue

            if agency and agency.id not in seen_agencies:
                total_income += agency.total_income or 0
                seen_agencies.add(agency.id)

        return total_income


class RetrieveTicketOrderSerializer(BaseTicketOrderSerializer):
    class Meta(BaseTicketOrderSerializer.Meta): ...


class UpdateTicketOrderSerializer(BaseTicketOrderSerializer):
    class Meta(BaseTicketOrderSerializer.Meta):
        fields = [
            "order_status",
        ]
