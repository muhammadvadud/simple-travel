from rest_framework import serializers
from core.apps.tickets.models import TicketsModel, TicketsImagesModel, TicketsAmenitiesModel, \
    TicketsIncludedServicesModel, \
    TicketsItineraryModel, TicketsItineraryDestinationsModel, TicketsItineraryImagesModel, TicketsHotelMealsModel, \
    TransportTicketModel, FullTransportInfoModel, FullTariff, TariffModel
from core.apps.tickets.models.hotel import HotelModel, HotelAmenitiesModel


class FullTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullTariff
        fields = [
            "tariff",
            "price",
        ]


class TicketImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsImagesModel
        fields = [
            "image"
        ]


class HotelAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelAmenitiesModel
        fields = [
            "name",
        ]


class TransportTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportTicketModel
        fields = [
            "name",
            "icon_name"
        ]


class FullTransportInfoSerializer(serializers.ModelSerializer):
    full_info = TransportTicketSerializer(read_only=True, many=False)

    class Meta:
        model = FullTransportInfoModel
        fields = [
            "price",
            "full_info",

        ]


class WriteFullTransportInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullTransportInfoModel
        fields = ["transport", "price"]


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields = [
            "name",
            "name_ru",
            "rating",
            "meal_plan",
            "hotel_type",
            "hotel_amenities",
            "hotel_features",
        ]


class TicketsHotelMealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsHotelMealsModel
        fields = ["image", "name", "name_ru", "desc", "desc_ru"]


class TicketsItineraryDestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsItineraryDestinationsModel
        fields = ["name", "name_ru"]


class TicketsItineraryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsItineraryImagesModel
        fields = ["image"]


class TicketsItinerarySerializer(serializers.ModelSerializer):
    ticket_itinerary_image = TicketsItineraryImagesSerializer(many=True, write_only=True)
    ticket_itinerary_destinations = TicketsItineraryDestinationsSerializer(many=True, write_only=True)

    class Meta:
        model = TicketsItineraryModel
        fields = ["title", "title_ru", "duration", "ticket_itinerary_image", "ticket_itinerary_destinations"]


class TicketsIncludedServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsIncludedServicesModel
        fields = [
            "image",
            "title",
            "title_ru",
            "desc",
            "desc_uz",
        ]


class TicketsAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsAmenitiesModel
        fields = [
            'name',
            'name_ru',
            'icon_name'

        ]


class BaseTicketsSerializer(serializers.ModelSerializer):
    hotel_name = serializers.SerializerMethodField()
    hotel_rating = serializers.SerializerMethodField()
    hotel_amenities = serializers.SerializerMethodField()

    ticket_amenities = TicketsAmenitiesSerializer(many=True, read_only=True)
    ticket_images = TicketImagesSerializer(many=True, read_only=True)
    ticket_included_services = TicketsIncludedServicesSerializer(many=True, read_only=True)
    ticket_itinerary = TicketsItinerarySerializer(many=True, read_only=True)
    ticket_hotel_meals = TicketsHotelMealsSerializer(many=True, read_only=True)
    transports = FullTransportInfoSerializer(many=True, read_only=True)
    tariff = FullTariffSerializer(many=True, write_only=True, required=True)

    class Meta:
        model = TicketsModel
        fields = [
            "id",
            "hotel_name",
            "hotel_rating",
            "hotel_amenities",
            "title",
            "title_ru",
            "price",
            "min_person",
            "max_person",
            "departure",
            "departure_ru",
            "destination",
            "destination_ru",
            "departure_time",
            "travel_time",
            "location_name",
            "location_name_ru",
            "passenger_count",
            "languages",
            "hotel_info",
            "hotel_info_ru",
            "duration_days",
            "rating",
            "hotel_meals",
            "hotel_meals_ru",
            "slug",
            "visa_required",
            "image_banner",
            "badge",
            "transports",
            "ticket_images",
            "ticket_amenities",
            "ticket_included_services",
            "ticket_itinerary",
            "ticket_hotel_meals",
            "tariff",
        ]

    def get_hotel_name(self, obj):
        hotel = obj.ticket_hotel.all().first()
        return hotel.name if hotel else None

    def get_hotel_rating(self, obj):
        hotel = obj.ticket_hotel.all().first()
        return hotel.rating if hotel else None

    def get_hotel_amenities(self, obj):
        hotel = obj.ticket_hotel.all().first()
        if not hotel:
            return []
        return [a.name for a in hotel.hotel_amenities.all()]


class ListTicketsSerializer(BaseTicketsSerializer):
    class Meta(BaseTicketsSerializer.Meta):
        fields = [
            "id",
            "destination",
            "duration_days",
            "hotel_name",
            "price",
            "duration_days",
            "duration_days",
            "hotel_rating",
            "hotel_amenities",
        ]


class RetrieveTicketsSerializer(BaseTicketsSerializer):
    class Meta(BaseTicketsSerializer.Meta):
        ref_name = "RetrieveDashboardTickets"


class CreateTicketsSerializer(BaseTicketsSerializer):
    ticket_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=True
    )
    ticket_amenities = TicketsAmenitiesSerializer(many=True, write_only=True, required=True)
    ticket_included_services = TicketsIncludedServicesSerializer(many=True, write_only=True, required=True)
    ticket_itinerary = TicketsItinerarySerializer(many=True, write_only=True, required=True)
    ticket_hotel_meals = TicketsHotelMealsSerializer(many=True, write_only=True, required=True)
    transports = WriteFullTransportInfoSerializer(many=True, write_only=True, required=False)
    tariff = FullTariffSerializer(many=True, write_only=True, required=True)
    badge = serializers.ListField(
        child=serializers.IntegerField(),
        required=True
    )

    class Meta(BaseTicketsSerializer.Meta):
        fields = [
            "id",
            "hotel_name",
            "hotel_rating",
            "hotel_amenities",
            "title",
            "title_ru",
            "price",
            "min_person",
            "max_person",
            "departure",
            "departure_ru",
            "destination",
            "destination_ru",
            "departure_time",
            "travel_time",
            "location_name",
            "location_name_ru",
            "passenger_count",
            "languages",
            "hotel_info",
            "hotel_info_ru",
            "duration_days",
            "rating",
            "hotel_meals",
            "hotel_meals_ru",
            "slug",
            "visa_required",
            "image_banner",
            "badge",
            "tariff",
            "ticket_images",
            "ticket_amenities",
            "ticket_included_services",
            "ticket_itinerary",
            "ticket_hotel_meals",
            "transports",
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["travel_agency"] = getattr(request.user, "travel_agency", None)

        badge_data = validated_data.pop("badge", [])
        ticket_images = validated_data.pop("ticket_images", [])
        ticket_amenities = validated_data.pop("ticket_amenities", [])
        ticket_included_services = validated_data.pop("ticket_included_services", [])
        ticket_itinerary = validated_data.pop("ticket_itinerary", [])
        ticket_hotel_meals = validated_data.pop("ticket_hotel_meals", [])
        transports = validated_data.pop("transports", [])
        tariffs = validated_data.pop("tariff", [])
        print(badge_data)
        print(ticket_images)
        print(ticket_amenities)
        print(ticket_included_services)
        print(ticket_itinerary)
        print(ticket_hotel_meals)
        print(transports)
        print(tariffs)

        ticket = TicketsModel.objects.create(**validated_data)

        if badge_data:
            print(f"ishlayapti badge {badge_data}")
            ticket.badge.set(badge_data)

        if ticket_images:
            TicketsImagesModel.objects.bulk_create(
                [TicketsImagesModel(image=image, ticket=ticket) for image in ticket_images]
            )
        if ticket_amenities:
            TicketsAmenitiesModel.objects.bulk_create(
                [TicketsAmenitiesModel(ticket=ticket, **amenity) for amenity in ticket_amenities]
            )
        if ticket_included_services:
            TicketsIncludedServicesModel.objects.bulk_create(
                [TicketsIncludedServicesModel(ticket=ticket, **service) for service in ticket_included_services]
            )
        if ticket_hotel_meals:
            TicketsHotelMealsModel.objects.bulk_create(
                [TicketsHotelMealsModel(ticket=ticket, **meal) for meal in ticket_hotel_meals]
            )
        if transports:
            full_transports = []
            for tr_data in transports:
                full_transport = FullTransportInfoModel.objects.create(
                    transport_id=tr_data["transport"],
                    price=tr_data["price"]
                )
                full_transports.append(full_transport)

            ticket.transports.set(full_transports)
        if tariffs:
            full_tariffs = []
            for tariff_data in tariffs:
                full_tariff = FullTariff.objects.create(**tariff_data)
                full_tariffs.append(full_tariff)

            ticket.tariff.set(full_tariffs)

        for itinerary_data in ticket_itinerary:
            itinerary_images = itinerary_data.pop("ticket_itinerary_image", [])
            itinerary_destinations = itinerary_data.pop("ticket_itinerary_destinations", [])
            itinerary = TicketsItineraryModel.objects.create(ticket=ticket, **itinerary_data)

            for img in itinerary_images:
                TicketsItineraryImagesModel.objects.create(tickets_itinerary=itinerary, **img)
            for dest in itinerary_destinations:
                TicketsItineraryDestinationsModel.objects.create(tickets_itinerary=itinerary, **dest)

        return ticket
