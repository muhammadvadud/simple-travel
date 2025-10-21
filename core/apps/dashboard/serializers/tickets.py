from rest_framework import serializers
from core.apps.tickets.models import TicketsModel, TicketsImagesModel, TicketsAmenitiesModel, \
    TicketsIncludedServicesModel, \
    TicketsItineraryModel, TicketsItineraryDestinationsModel, TicketsItineraryImagesModel, TicketsHotelMealsModel
from core.apps.tickets.models.hotel import HotelModel


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

    class Meta:
        model = TicketsModel
        fields = [
            "id",
            "destination",
            "duration_days",
            "hotel_name",
            "price",
            "duration_days",
            "duration_days",
        ]


class ListTicketsSerializer(BaseTicketsSerializer):
    class Meta(BaseTicketsSerializer.Meta): ...


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

    # ticket_hotel = HotelSerializer(many=True, write_only=True, required=True)
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
            "hotel_meals",
            "hotel_meals_ru",
            "slug",
            "visa_required",
            "image_banner",
            "badge",
            #######
            "ticket_images",
            "ticket_amenities",
            "ticket_included_services",
            "ticket_itinerary",
            "ticket_hotel_meals",

        ]

    def create(self, validated_data):
        validated_data['travel_agency'] = self.context.get('request').user.travel_agency.id
        ticket_images = self.validated_data.pop("ticket_images", [])
        print(f"ticket_images>>>>>>>>>>>>>>>>>>{ticket_images}")
        ticket_amenities = self.validated_data.pop("ticket_amenities", [])
        print(f"ticket_amenities>>>>>>>>>>>>>>>>>>{ticket_amenities}")
        ticket_included_services = self.validated_data.pop("ticket_included_services", [])
        print(f"ticket_included_services>>>>>>>>>>>>>>>>>>{ticket_included_services}")
        ticket_itinerary = self.validated_data.pop("ticket_itinerary", [])
        print(f"ticket_itinerary>>>>>>>>>>>>>>>>>>{ticket_itinerary}")
        ticket_hotel_meals = self.validated_data.pop("ticket_hotel_meals", [])
        print(f"ticket_itinerary>>>>>>>>>>>>>>>>>>{ticket_hotel_meals}")
        ticket = TicketsModel.objects.create(**validated_data)
        for ticket_image in ticket_images:
            TicketsImagesModel.objects.create(image=ticket_image, ticket=ticket)
        for ticket_amenities in ticket_amenities:
            TicketsAmenitiesModel.objects.create(**ticket_amenities)
        for ticket_included_services in ticket_included_services:
            TicketsIncludedServicesModel.objects.create(**ticket_included_services)
        for ticket_itinerary in ticket_itinerary:
            TicketsItineraryModel.objects.create(**ticket_itinerary)
        for ticket_hotel_meals in ticket_hotel_meals:
            TicketsHotelMealsModel.objects.create(**ticket_hotel_meals)
        return ticket
