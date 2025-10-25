from rest_framework import serializers
from core.apps.tickets.models import TicketsModel, TicketsImagesModel, TicketsAmenitiesModel, \
    TicketsIncludedServicesModel, \
    TicketsItineraryModel, TicketsItineraryDestinationsModel, TicketsItineraryImagesModel, TicketsHotelMealsModel, \
    TransportTicketModel, FullTransportInfoModel, FullTariff, TariffModel, BadgeModel
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
        required=False,
        write_only=True
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

    def validate_badge(self, value):
        """
        Badge ID listini tekshiradi — mavjud bo'lmagan idlar bo'lsa ValidationError.
        """
        from core.apps.tickets.models import BadgeModel

        if not isinstance(value, (list, tuple)):
            raise serializers.ValidationError("badge maydoni ro'yxat bo'lishi kerak.")

        existing_ids = set(BadgeModel.objects.filter(id__in=value).values_list("id", flat=True))
        missing = set(value) - existing_ids
        if missing:
            raise serializers.ValidationError(f"Ushbu badge ID(lar) topilmadi: {sorted(missing)}")
        return value

    def _safe_pop_field(self, data: dict, field_name: str, default=None):

        val = data.pop(field_name, default)

        if val is None:
            return default

        if isinstance(val, (list, tuple)):
            return list(val)

        if hasattr(val, "all") and callable(getattr(val, "all")):
            try:
                qs = val.all()
            except Exception:
                return default

            if field_name == "badge":
                try:
                    return list(qs.values_list("id", flat=True))
                except Exception:
                    return [getattr(obj, "id", None) for obj in list(qs) if getattr(obj, "id", None) is not None]

            return []

        return default

    def create(self, validated_data):
        from core.apps.tickets.models import (
            BadgeModel,
            TicketsImagesModel,
            TicketsAmenitiesModel,
            TicketsIncludedServicesModel,
            TicketsItineraryModel,
            TicketsItineraryImagesModel,
            TicketsItineraryDestinationsModel,
            TicketsHotelMealsModel,
            FullTransportInfoModel,
            FullTariff,
            TicketsModel,
        )

        request = self.context.get("request")
        validated_data["travel_agency"] = getattr(request.user, "travel_agency", None)

        # Xavfsiz pop — manager/descriptor tushib qolsa ham boshqaramiz
        badge_data = self._safe_pop_field(validated_data, "badge", default=[])
        ticket_images = self._safe_pop_field(validated_data, "ticket_images", default=[])
        ticket_amenities = self._safe_pop_field(validated_data, "ticket_amenities", default=[])
        ticket_included_services = self._safe_pop_field(validated_data, "ticket_included_services", default=[])
        ticket_itinerary = self._safe_pop_field(validated_data, "ticket_itinerary", default=[])
        ticket_hotel_meals = self._safe_pop_field(validated_data, "ticket_hotel_meals", default=[])
        transports = self._safe_pop_field(validated_data, "transports", default=[])
        tariffs = self._safe_pop_field(validated_data, "tariff", default=[])
        ticket = TicketsModel.objects.create(**validated_data)

        if badge_data:
            existing_badges = BadgeModel.objects.filter(id__in=badge_data)
            if existing_badges.exists():
                ticket.badge.set(existing_badges)
            else:
                raise serializers.ValidationError({"badge": "Yuborilgan badge ID(lar) topilmadi yoki mavjud emas."})

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
                if not isinstance(tr_data, dict):
                    continue

                transport_value = tr_data.get("transport")

                if isinstance(transport_value, dict):
                    transport_id = transport_value.get("id")
                elif hasattr(transport_value, "id"):
                    transport_id = transport_value.id
                else:
                    transport_id = transport_value

                full_transport = FullTransportInfoModel.objects.create(
                    transport_id=transport_id,
                    price=tr_data.get("price")
                )
                full_transports.append(full_transport)

            if full_transports:
                ticket.transports.set(full_transports)

        if tariffs:
            full_tariffs = []
            for tariff_data in tariffs:
                if not isinstance(tariff_data, dict):
                    continue

                tariff_value = tariff_data.get("tariff")

                if hasattr(tariff_value, "id"):
                    tariff_id = tariff_value.id
                else:
                    tariff_id = tariff_value

                full_tariff = FullTariff.objects.create(
                    tariff_id=tariff_id,
                    price=tariff_data.get("price")
                )
                full_tariffs.append(full_tariff)

            if full_tariffs:
                ticket.tariff.set(full_tariffs)
        for itinerary_data in ticket_itinerary:
            if not isinstance(itinerary_data, dict):
                continue

            itinerary_images = itinerary_data.pop("ticket_itinerary_image", []) or []
            itinerary_destinations = itinerary_data.pop("ticket_itinerary_destinations", []) or []
            itinerary = TicketsItineraryModel.objects.create(ticket=ticket, **itinerary_data)

            if itinerary_images:
                TicketsItineraryImagesModel.objects.bulk_create(
                    [TicketsItineraryImagesModel(tickets_itinerary=itinerary, **img) for img in itinerary_images]
                )

            if itinerary_destinations:
                TicketsItineraryDestinationsModel.objects.bulk_create(
                    [TicketsItineraryDestinationsModel(tickets_itinerary=itinerary, **dest) for dest in
                     itinerary_destinations]
                )

        return ticket
