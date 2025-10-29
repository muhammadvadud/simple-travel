from rest_framework import serializers
from core.apps.accounts.models import User
from core.apps.accounts.serializers.user import UserSerializer
from collections import Counter

from core.apps.tickets.models import (
    TicketsAmenitiesModel,
    TicketsCommentsModel,
    TicketsHotelMealsModel,
    TicketsImagesModel,
    TicketsIncludedServicesModel,
    TicketsItineraryDestinationsModel,
    TicketsItineraryImagesModel,
    TicketsItineraryModel,
    TicketsModel,
    TicketorderModel
)
from core.apps.tickets.models.tariff import TariffModel, FullTariff
from core.apps.tickets.serializers.badge.badge import ListBadgeSerializer


class TicketsTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = TariffModel
        fields = ["name"]


class TicketsFullTariffSerializer(serializers.ModelSerializer):
    tariff = TicketsTariffSerializer(read_only=True)

    class Meta:
        model = FullTariff
        fields = ["tariff", "price"]


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
            "desc",
        ]


class TicketsAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsAmenitiesModel
        fields = ["name", "icon_name"]


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
    tariff = TicketsFullTariffSerializer(many=True, read_only=True)
    is_liked = serializers.SerializerMethodField()
    travel_agency_id = serializers.SerializerMethodField()
    allow_comment = serializers.SerializerMethodField()

    class Meta:
        model = TicketsModel
        fields = [
            "id",
            "title",
            "price",
            "min_person",
            "max_person",
            "price",
            "departure",
            "destination",
            "passenger_count",
            "languages",
            "rating",
            "hotel_info",
            "duration_days",
            "hotel_meals",
            "ticket_images",
            "ticket_amenities",
            "ticket_included_services",
            "ticket_itinerary",
            "ticket_hotel_meals",
            "travel_agency_id",
            "ticket_comments",
            "tariff",
            "is_liked",
            "allow_comment",
            "featured_tickets",
        ]

    def get_is_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.ticket_like.filter(user=user).exists()
        return False

    def get_travel_agency_id(self, obj):
        travel_id = getattr(obj.travel_agency, "custom_id", None)
        if travel_id is not None:
            return f"{travel_id}"
        return None

    def get_allow_comment(self, obj):
        request = self.context.get("request")
        user = getattr(request, "user", None)

        if not user or not user.is_authenticated:
            return False

        return TicketorderModel.objects.filter(
            user=user,
            ticket_id=obj.id,
            order_status__in=["confirmed", "completed"]
        ).exists()


class ListTicketsSerializer(BaseTicketsSerializer):
    ticket_images = serializers.SerializerMethodField()
    ticket_amenities = TicketsAmenitiesSerializer(many=True, read_only=True)
    badge = ListBadgeSerializer(many=True, read_only=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = TicketsModel
        fields = [
            "id",
            "title",
            "price",
            "travel_time",
            "departure",
            "passenger_count",
            "rating",
            "duration_days",
            "destination",
            "ticket_images",
            "ticket_amenities",
            "passenger_count",
            "badge",
            "visa_required",
            "is_liked",
            "featured_tickets",
        ]

    def get_ticket_images(self, obj):
        image = obj.image_banner
        if image:
            return image.url
        return None

    def get_is_liked(self, obj):
        user = self.context["request"].user
        if user.is_authenticated:
            return obj.ticket_like.filter(user=user).exists()
        return False


class FullInformationTicketsSerializer(serializers.Serializer):
    tickets = serializers.SerializerMethodField()
    min_price = serializers.SerializerMethodField()
    max_price = serializers.SerializerMethodField()
    top_duration = serializers.SerializerMethodField()
    top_destinations = serializers.SerializerMethodField()
    hotel_features_by_type = serializers.SerializerMethodField()
    hotel_types = serializers.SerializerMethodField()
    hotel_amenities = serializers.SerializerMethodField()

    def get_tickets(self, queryset):
        return ListTicketsSerializer(queryset, many=True, context=self.context).data

    def get_min_price(self, obj):
        products = obj
        if not products:
            return None
        return min([p.price for p in products])

    def get_max_price(self, obj):
        products = obj
        if not products:
            return None
        return max([p.price for p in products])

    def get_top_duration(self, obj):
        from collections import Counter

        qs = obj

        duration_days_list = [
            t.duration_days for t in qs if getattr(t, "duration_days", None) is not None
        ]
        counter = Counter(duration_days_list)

        return [{"duration": val} for val, _ in counter.most_common(3)]

    def get_top_destinations(self, obj):
        from collections import Counter
        qs = obj

        destination_list = [
            t.destination for t in qs if getattr(t, "destination", None) is not None
        ]
        counter = Counter(destination_list)
        return [{"destination": val} for val, _ in counter.most_common(5)]

    def get_hotel_features_by_type(self, obj):
        from collections import defaultdict

        qs = obj
        features_map = defaultdict(list)

        for ticket in qs:
            for hotel in ticket.ticket_hotel.all():
                for feature in hotel.hotel_features.all():
                    features_map[feature.feature_type.hotel_feature_type_name].append(
                        feature.feature_name
                    )

        return [
            {"type": type_name, "features": list(set(features))}
            for type_name, features in features_map.items()
        ]

    def get_hotel_types(self, obj):
        types = set()
        for ticket in obj:
            for hotel in ticket.ticket_hotel.all():
                for htype in hotel.hotel_type.all():
                    types.add(htype.name)
        return list(types)

    def get_hotel_amenities(self, obj):
        amenities = set()
        for ticket in obj:
            for hotel in ticket.ticket_hotel.all():
                for amenity in hotel.hotel_amenities.all():
                    amenities.add(amenity.name)
        return list(amenities)


class RetrieveTicketsSerializer(BaseTicketsSerializer):
    class Meta(BaseTicketsSerializer.Meta): ...


class CreateTicketsSerializer(BaseTicketsSerializer):
    class Meta(BaseTicketsSerializer.Meta):
        fields = [
            "id",
            "title",
            "price",
            "departure",
            "destination",
            "passenger_count",
            "rating",
            "hotel_info",
            "duration_days",
            "hotel_meals",
        ]
