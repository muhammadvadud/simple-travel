from rest_framework import serializers
from core.apps.tickets.models import TicketsModel, TicketsImagesModel, TicketsAmenitiesModel, \
    TicketsIncludedServicesModel, TicketsItineraryModel, TicketsItineraryImagesModel, TicketsItineraryDestinationsModel, \
    TicketsHotelMealsModel, TicketsCommentsModel
from core.apps.accounts.models import User
from core.apps.accounts.serializers.user import UserSerializer
from core.apps.tickets.models.tariff import TariffModel
from core.apps.tickets.serializers.badge.badge import ListBadgeSerializer



class TicketsTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffModel
        fields = ['name']


class CommentUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class TicketsCommentsSerializer(serializers.ModelSerializer):
    user = CommentUserSerializer(read_only=True)

    class Meta:
        model = TicketsCommentsModel
        fields = ["user", "text", "rating"]


class TicketsHotelMealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsHotelMealsModel
        fields = ["image", "name", "desc"]


class TicketsItineraryDestinationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsItineraryDestinationsModel
        fields = ['name']


class TicketsItineraryImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsItineraryImagesModel
        fields = ['image']


class TicketsItinerarySerializer(serializers.ModelSerializer):
    ticket_itinerary_image = TicketsItineraryImagesSerializer(many=True, read_only=True)
    ticket_itinerary_destinations = TicketsItineraryDestinationsSerializer(many=True, read_only=True)

    class Meta:
        model = TicketsItineraryModel
        fields = ["title", "duration", "ticket_itinerary_image", "ticket_itinerary_destinations"]


class TicketsIncludedServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsIncludedServicesModel
        fields = ["image", "title", "desc", ]


class TicketsAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsAmenitiesModel
        fields = ["name"]


class TicketsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsImagesModel
        fields = ["image"]


class BaseTicketsSerializer(serializers.ModelSerializer):
    ticket_images = TicketsImageSerializer(many=True, read_only=True)
    ticket_amenities = TicketsAmenitiesSerializer(many=True, read_only=True)
    ticket_included_services = TicketsIncludedServicesSerializer(many=True, read_only=True)
    ticket_itinerary = TicketsItinerarySerializer(many=True, read_only=True)
    ticket_hotel_meals = TicketsHotelMealsSerializer(many=True, read_only=True)
    ticket_comments = TicketsCommentsSerializer(many=True, read_only=True)
    tariff = TicketsTariffSerializer(many=True, read_only=True)

    class Meta:
        model = TicketsModel
        fields = [
            "id",
            "title",
            "price",
            "departure_date",
            "departure",
            "destination",
            "passenger_count",
            "rating",
            "hotel_info",
            "duration_days",
            "hotel_meals",
            "ticket_images",
            "ticket_amenities",
            "ticket_included_services",
            "ticket_itinerary",
            "ticket_hotel_meals",
            "ticket_comments",
            "tariff",

        ]


class ListTicketsSerializer(BaseTicketsSerializer):
    ticket_images = serializers.SerializerMethodField()
    ticket_amenities = TicketsAmenitiesSerializer(many=True, read_only=True)
    badge = ListBadgeSerializer(many=True, read_only=True)

    class Meta:
        model = TicketsModel
        fields = [
            "id",
            "title",
            "price",
            "departure_date",
            "departure",
            "passenger_count",
            "rating",
            "duration_days",
            "destination",
            "ticket_images",
            "ticket_amenities",
            "passenger_count",
            "badge",
            "visa_required"
        ]

    def get_ticket_images(self, obj):
        image = obj.ticket_images.first()
        if image:
            return TicketsImageSerializer(image).data
        return None


class RetrieveTicketsSerializer(BaseTicketsSerializer):
    class Meta(BaseTicketsSerializer.Meta): ...


class CreateTicketsSerializer(BaseTicketsSerializer):
    class Meta(BaseTicketsSerializer.Meta):
        fields = [
            "id",
            "title",
            "price",
            "departure_date",
            "departure",
            "destination",
            "passenger_count",
            "rating",
            "hotel_info",
            "duration_days",
            "hotel_meals",
        ]
