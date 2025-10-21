from rest_framework import serializers
from core.apps.tickets.models import TicketsModel, TicketsAmenitiesModel, TicketsIncludedServicesModel, \
    TicketsItineraryModel, TicketsItineraryDestinationsModel,TicketsItineraryImagesModel


class TicketsItineraryDestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsItineraryDestinationsModel
        fields = ["name"]


class TicketsItineraryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsItineraryImagesModel
        fields = ["image"]


class TicketsItinerarySerializer(serializers.ModelSerializer):
    ticket_itinerary_image = TicketsItineraryImagesSerializer(many=True, read_only=True)
    ticket_itinerary_destinations = TicketsItineraryDestinationsSerializer(many=True, read_only=True)

    class Meta:
        model = TicketsItineraryModel
        fields = ["title", "duration", "ticket_itinerary_image", "ticket_itinerary_destinations"]


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

    class Meta(BaseTicketsSerializer.Meta):
        fields = [
            "id",
            "travel_agency",
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

        ]

    def create(self, validated_data):
        ticket_images = self.validated_data.pop("ticket_images", [])
        print(f"ticket_images>>>>>>>>>>>>>>>>>>{ticket_images}")
        ticket_amenities = self.validated_data.pop("ticket_amenities", [])
        print(f"ticket_images>>>>>>>>>>>>>>>>>>{ticket_amenities}")
        ticket_included_services = self.validated_data.pop("ticket_included_services", [])
        print(f"ticket_images>>>>>>>>>>>>>>>>>>{ticket_included_services}")
