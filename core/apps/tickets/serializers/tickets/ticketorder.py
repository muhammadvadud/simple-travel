from rest_framework import serializers
from core.apps.tickets.models import TicketorderModel, TicketsModel, PaidServicesModel, ExtraServicesModel, \
    TransportTicketModel

from core.apps.accounts.models import ParticipantModel
from core.apps.accounts.serializers.participant.participant import ListParticipantSerializer
from core.apps.tickets.serializers import ListExtraServicesSerializer, ListPaidServicesSerializer
from ..tickets.tickets import TicketsAmenitiesSerializer, TicketsTariffSerializer


class OrderTicketSerializer(serializers.ModelSerializer):
    service_name = serializers.SerializerMethodField()

    class Meta:
        model = TicketsModel
        fields = ['id', "service_name", "location_name"]

    def get_service_name(self, obj):
        return f"{obj.departure}-{obj.destination}"


class BaseTicketorderSerializer(serializers.ModelSerializer):
    ticket = OrderTicketSerializer(read_only=True)
    participant = ListParticipantSerializer(many=True, read_only=True)
    extra_service = ListExtraServicesSerializer(many=True, read_only=True)
    extra_paid_service = ListPaidServicesSerializer(many=True, read_only=True)

    class Meta:
        model = TicketorderModel
        fields = [
            "id",
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
            "total_price",
        ]


class ListTicketorderSerializer(BaseTicketorderSerializer):
    class Meta(BaseTicketorderSerializer.Meta): ...


class RetrieveTicketorderSerializer(BaseTicketorderSerializer):
    class Meta(BaseTicketorderSerializer.Meta): ...


class CreateTicketorderSerializer(BaseTicketorderSerializer):
    participant = serializers.PrimaryKeyRelatedField(many=True, queryset=ParticipantModel.objects.all(), required=False)
    extra_service = serializers.PrimaryKeyRelatedField(many=True, queryset=ExtraServicesModel.objects.all(),
                                                       required=False)
    extra_paid_service = serializers.PrimaryKeyRelatedField(many=True, queryset=PaidServicesModel.objects.all(),
                                                            required=False)
    ticket = serializers.PrimaryKeyRelatedField(
        queryset=TicketsModel.objects.all(), required=True)

    class Meta(BaseTicketorderSerializer.Meta):
        fields = [
            "id",
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
            "total_price",
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        if request and request.user and request.user.is_authenticated:
            validated_data["user"] = request.user
        else:
            raise serializers.ValidationError({"user": "User is required"})

        participants_data = validated_data.pop("participant", [])
        extra_services_data = validated_data.pop("extra_service", [])
        extra_paid_services_data = validated_data.pop("extra_paid_service", [])
        ticketorder = TicketorderModel.objects.create(**validated_data)
        if participants_data:
            ticketorder.participant.set(participants_data)

        if extra_services_data:
            ticketorder.extra_service.set(extra_services_data)

        if extra_paid_services_data:
            ticketorder.extra_paid_service.set(extra_paid_services_data)

        return ticketorder


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportTicketModel
        fields = [
            "name",
            "icon_name"
        ]


class GetTicketInfoOrderCreateSerializer(serializers.ModelSerializer):
    ticket_amenities = TicketsAmenitiesSerializer(many=True, read_only=True)
    tariff = TicketsTariffSerializer(many=True, read_only=True)
    transports = TransportSerializer(many=True, read_only=True)
    extra_service = ListExtraServicesSerializer(source="ticket_extra_service", many=True, read_only=True)
    extra_paid_service = ListPaidServicesSerializer(source="ticket_extra_paid_service", many=True, read_only=True)

    class Meta:
        model = TicketsModel
        fields = [
            "title",
            "price",
            "departure",
            "destination",
            "departure_date",
            "departure_time",
            "travel_time",
            "image_banner",
            "rating",
            "ticket_amenities",
            "tariff",
            "transports",
            "extra_service",
            "extra_paid_service",
        ]
