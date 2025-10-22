from rest_framework import serializers
from core.apps.tickets.models import TicketsModel, TicketsImagesModel, TicketsAmenitiesModel, \
    TicketsIncludedServicesModel, \
    TicketsItineraryModel, TicketsItineraryDestinationsModel, TicketsItineraryImagesModel, TicketsHotelMealsModel, \
    TransportTicketModel, FullTransportInfoModel
from core.apps.tickets.models.hotel import HotelModel


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
    hotel_name = serializers.CharField(source="tickets__ticket_hotel__name", read_only=True)
    hotel_rating = serializers.FloatField(source="tickets__ticket_hotel__rating", read_only=True)
    hotel_aminates = serializers.CharField(source="tickets__ticket_amenities__name", read_only=True)
    ticket_amenities = TicketsAmenitiesSerializer(many=True, read_only=True)
    ticket_images = serializers.ListField(
        child=serializers.ImageField(),
        read_only=True
    )
    ticket_included_services = TicketsIncludedServicesSerializer(many=True, read_only=True)
    ticket_itinerary = TicketsItinerarySerializer(many=True, read_only=True)
    ticket_hotel_meals = TicketsHotelMealsSerializer(many=True, read_only=True)
    transports = FullTransportInfoSerializer(many=True, read_only=True)

    class Meta:
        model = TicketsModel
        fields = [
            "id",
            "hotel_name",
            "hotel_rating",
            "hotel_aminates",
            "title",
            "price",
            "min_person",
            "max_person",
            "departure",
            "destination",
            "departure_time",
            "travel_time",
            "location_name",
            "passenger_count",
            "languages",
            "hotel_info",
            "duration_days",
            "rating",
            "hotel_meals",
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
        ]


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
            "hotel_aminates",
        ]


class RetrieveTicketsSerializer(BaseTicketsSerializer):
    class Meta(BaseTicketsSerializer.Meta): ...


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

    class Meta(BaseTicketsSerializer.Meta):
        fields = [
            "id",
            "hotel_name",
            "hotel_rating",
            "hotel_aminates",
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
        ]

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['travel_agency'] = request.user.travel_agency

        badge_data = validated_data.pop("badge", [])

        ticket_images = validated_data.pop("ticket_images", [])
        ticket_amenities = validated_data.pop("ticket_amenities", [])
        ticket_included_services = validated_data.pop("ticket_included_services", [])
        ticket_itinerary = validated_data.pop("ticket_itinerary", [])
        ticket_hotel_meals = validated_data.pop("ticket_hotel_meals", [])

        ticket = TicketsModel.objects.create(**validated_data)

        if badge_data:
            ticket.badge.set(badge_data)

        for image in ticket_images:
            TicketsImagesModel.objects.create(image=image, ticket=ticket)

        for amenity in ticket_amenities:
            TicketsAmenitiesModel.objects.create(ticket=ticket, **amenity)

        for service in ticket_included_services:
            TicketsIncludedServicesModel.objects.create(ticket=ticket, **service)

        for itinerary in ticket_itinerary:
            TicketsItineraryModel.objects.create(ticket=ticket, **itinerary)

        for meal in ticket_hotel_meals:
            TicketsHotelMealsModel.objects.create(ticket=ticket, **meal)

        return ticket
