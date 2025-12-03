from rest_framework import serializers
from core.apps.tickets.models import TicketorderModel, TicketsModel, PaidServicesModel, ExtraServicesModel, \
    TransportTicketModel, FullTransportInfoModel, Region, Country

from core.apps.accounts.models import ParticipantModel
from core.apps.accounts.serializers.participant.participant import ListParticipantSerializer
from core.apps.tickets.serializers import ListExtraServicesSerializer, ListPaidServicesSerializer
from ..tickets.tickets import TicketsAmenitiesSerializer, TicketsFullTariffSerializer
from core.utils.order_pdf_creator import creator_pdf


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            "id",
            "name"
        ]


class RegionSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)

    class Meta:
        model = Region
        fields = [
            "id",
            "name",
            "country"
        ]


class OrderTicketSerializer(serializers.ModelSerializer):
    service_name = serializers.SerializerMethodField()

    class Meta:
        model = TicketsModel
        fields = ['id', "title", "service_name", "location_name"]

    def get_service_name(self, obj):
        return f"{obj.departure}-{obj.destination}"


class BaseTicketorderSerializer(serializers.ModelSerializer):
    ticket = OrderTicketSerializer(read_only=True)
    participant = ListParticipantSerializer(many=True, read_only=True)
    extra_service = ListExtraServicesSerializer(many=True, read_only=True)
    extra_paid_service = ListPaidServicesSerializer(many=True, read_only=True)
    departure = RegionSerializer(read_only=True)
    destination = RegionSerializer(read_only=True)

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
            "order_status",
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
    departure = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(), required=True)
    destination = serializers.PrimaryKeyRelatedField(queryset=Region.objects.all(), required=True)

    class Meta(BaseTicketorderSerializer.Meta):
        fields = [
            "id",
            "departure",
            "destination",
            "departure_date",
            "arrival_time",
            "participant",
            "ticket",
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


class FullTransportSerializer(serializers.ModelSerializer):
    transport = TransportSerializer(read_only=True)

    class Meta:
        model = FullTransportInfoModel
        fields = [
            "transport",
            "price"
        ]


class GetTicketInfoOrderCreateSerializer(serializers.ModelSerializer):
    ticket_amenities = TicketsAmenitiesSerializer(many=True, read_only=True)
    transports = FullTransportSerializer(many=True, read_only=True)
    extra_service = ListExtraServicesSerializer(many=True, read_only=True)
    paid_extra_service = ListPaidServicesSerializer(many=True, read_only=True)
    hotel_rating = serializers.SerializerMethodField()
    departure = RegionSerializer(read_only=True)
    destination = RegionSerializer(read_only=True)

    class Meta:
        model = TicketsModel
        fields = [
            "title",
            "price",
            "departure",
            "destination",
            "departure_time",
            "min_person",
            "max_person",
            "travel_time",
            "image_banner",
            "rating",
            "ticket_amenities",
            "transports",
            "extra_service",
            "paid_extra_service",
            "hotel_rating",
        ]

    def get_hotel_rating(self, obj):
        hotel = obj.ticket_hotel.first()
        rating = hotel.rating
        if rating:
            return rating
        return None


class GetOrderPdfSerializer(serializers.Serializer):
    lang = serializers.CharField(write_only=True, required=True)
    order_id = serializers.CharField(write_only=True, required=True)
    file_path = serializers.SerializerMethodField()

    def create(self, validated_data):
        order_id = validated_data["order_id"]
        lang = validated_data["lang"]
        file_path = creator_pdf(order_id, lang)
        return {"file_path": file_path}
