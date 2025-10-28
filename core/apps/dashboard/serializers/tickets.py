from rest_framework import serializers
from core.apps.tickets.models import (
    TicketsModel, TicketsImagesModel, TicketsAmenitiesModel, TicketsIncludedServicesModel,
    TicketsItineraryModel, TicketsItineraryDestinationsModel, TicketsItineraryImagesModel,
    TicketsHotelMealsModel, TransportTicketModel, FullTransportInfoModel, FullTariff,
    PaidServicesModel, ExtraServicesModel
)
from core.apps.tickets.models.hotel import HotelModel, HotelAmenitiesModel


# ------------------ PAID / EXTRA SERVICES ------------------

class PaidExtraServicesReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidServicesModel
        fields = [
            "name",
            "name_ru",
            "name_uz",
            "price",
        ]


class PaidExtraServicesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaidServicesModel
        fields = [
            "name",
            "name_ru",
            "price",
        ]


class ExtraServicesReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraServicesModel
        fields = [
            "name",
            "name_ru",
            "name_uz",
        ]


class ExtraServicesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExtraServicesModel
        fields = [
            "name",
            "name_ru",
        ]


# ------------------ FULL TARIFF ------------------

class FullTariffReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullTariff
        fields = [
            "tariff",
            "price",
        ]


class FullTariffWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullTariff
        fields = [
            "tariff",
            "price",
        ]


# ------------------ IMAGES ------------------

class TicketImagesReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsImagesModel
        fields = ["image"]


class TicketImagesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsImagesModel
        fields = ["image"]


# ------------------ HOTEL AMENITIES ------------------

class HotelAmenitiesReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelAmenitiesModel
        fields = [
            "name",
            "name_ru",
            "name_uz",
        ]


class HotelAmenitiesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelAmenitiesModel
        fields = ["name", "name_ru"]


# ------------------ TRANSPORT ------------------

class TransportTicketReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportTicketModel
        fields = ["name", "icon_name"]


class TransportTicketWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportTicketModel
        fields = ["name", "icon_name"]


class FullTransportInfoReadSerializer(serializers.ModelSerializer):
    transport = TransportTicketReadSerializer(read_only=True)

    class Meta:
        model = FullTransportInfoModel
        fields = ["price", "transport"]


class FullTransportInfoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullTransportInfoModel
        fields = ["transport", "price"]


# ------------------ HOTEL ------------------

class HotelReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields = [
            "name",
            "name_ru",
            "name_uz",
            "rating",
            "meal_plan",
            "hotel_type",
            "hotel_amenities",
            "hotel_features",
        ]


class HotelWriteSerializer(serializers.ModelSerializer):
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


# ------------------ HOTEL MEALS ------------------

class TicketsHotelMealsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsHotelMealsModel
        fields = ["image", "name", "name_ru", "name_uz", "desc", "desc_ru", "desc_uz"]


class TicketsHotelMealsWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsHotelMealsModel
        fields = ["image", "name", "name_ru", "desc", "desc_ru"]


# ------------------ ITINERARY ------------------

class TicketsItineraryDestinationsReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsItineraryDestinationsModel
        fields = ["name", "name_ru", "name_uz"]


class TicketsItineraryDestinationsWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsItineraryDestinationsModel
        fields = ["name", "name_ru"]


class TicketsItineraryImagesReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsItineraryImagesModel
        fields = ["image"]


class TicketsItineraryImagesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsItineraryImagesModel
        fields = ["image"]


class TicketsItineraryReadSerializer(serializers.ModelSerializer):
    ticket_itinerary_image = TicketsItineraryImagesReadSerializer(many=True, read_only=True)
    ticket_itinerary_destinations = TicketsItineraryDestinationsReadSerializer(many=True, read_only=True)

    class Meta:
        model = TicketsItineraryModel
        fields = ["title", "title_ru", "title_uz", "duration", "ticket_itinerary_image",
                  "ticket_itinerary_destinations"]


class TicketsItineraryWriteSerializer(serializers.ModelSerializer):
    ticket_itinerary_image = TicketsItineraryImagesWriteSerializer(many=True, write_only=True)
    ticket_itinerary_destinations = TicketsItineraryDestinationsWriteSerializer(many=True, write_only=True)

    class Meta:
        model = TicketsItineraryModel
        fields = ["title", "title_ru", "duration", "ticket_itinerary_image", "ticket_itinerary_destinations"]


# ------------------ INCLUDED SERVICES ------------------

class TicketsIncludedServicesReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsIncludedServicesModel
        fields = [
            "image",
            "title",
            "title_ru",
            "title_uz",
            "desc",
            "desc_ru",
            "desc_uz",
        ]


class TicketsIncludedServicesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsIncludedServicesModel
        fields = [
            "image",
            "title",
            "title_ru",
            "desc",
            "desc_ru",
            "desc_uz",
        ]


# ------------------ AMENITIES ------------------

class TicketsAmenitiesReadSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsAmenitiesModel
        fields = ['name', 'name_ru', 'name_uz', 'icon_name']


class TicketsAmenitiesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsAmenitiesModel
        fields = ['name', 'name_ru', 'icon_name']


class BaseTicketsSerializer(serializers.ModelSerializer):
    hotel_name = serializers.SerializerMethodField()
    hotel_rating = serializers.SerializerMethodField()
    hotel_amenities = serializers.SerializerMethodField()

    ticket_amenities = TicketsAmenitiesReadSerializer(many=True, read_only=True)
    ticket_images = TicketImagesReadSerializer(many=True, read_only=True)
    ticket_included_services = TicketsIncludedServicesReadSerializer(many=True, read_only=True)
    ticket_itinerary = TicketsItineraryReadSerializer(many=True, read_only=True)
    ticket_hotel_meals = TicketsHotelMealsReadSerializer(many=True, read_only=True)
    transports = FullTransportInfoReadSerializer(many=True, read_only=True)
    tariff = FullTariffReadSerializer(many=True, read_only=True)
    extra_service = ExtraServicesReadSerializer(many=True, read_only=True)
    paid_extra_service = PaidExtraServicesReadSerializer(many=True, read_only=True)

    class Meta:
        model = TicketsModel
        fields = [
            "id",
            "hotel_name",
            "hotel_rating",
            "hotel_amenities",
            "title",
            "title_ru",
            "title_uz",
            "price",
            "min_person",
            "max_person",
            "departure",
            "departure_ru",
            "departure_uz",
            "destination",
            "destination_ru",
            "destination_uz",
            "departure_time",
            "travel_time",
            "location_name",
            "location_name_ru",
            "location_name_uz",
            "passenger_count",
            "languages",
            "hotel_info",
            "hotel_info_ru",
            "hotel_info_uz",
            "duration_days",
            "rating",
            "hotel_meals",
            "hotel_meals_ru",
            "hotel_meals_uz",
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
            "extra_service",
            "paid_extra_service",

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
    class Meta(BaseTicketsSerializer.Meta): ...


class CreateTicketsSerializer(BaseTicketsSerializer):
    ticket_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=True
    )
    ticket_amenities = TicketsAmenitiesWriteSerializer(many=True, write_only=True, required=True)
    ticket_included_services = TicketsIncludedServicesWriteSerializer(many=True, write_only=True, required=True)
    ticket_itinerary = TicketsItineraryWriteSerializer(many=True, write_only=True, required=True)
    ticket_hotel_meals = TicketsHotelMealsWriteSerializer(many=True, write_only=True, required=True)
    transports = FullTransportInfoWriteSerializer(many=True, write_only=True, required=False)
    tariff = FullTariffWriteSerializer(many=True, write_only=True, required=True)

    badge = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        write_only=True
    )
    extra_service = ExtraServicesWriteSerializer(many=True, write_only=True)
    paid_extra_service = PaidExtraServicesWriteSerializer(many=True, write_only=True)

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
            "extra_service",
            "paid_extra_service",
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

        badge_data = self._safe_pop_field(validated_data, "badge", default=[])
        ticket_images = self._safe_pop_field(validated_data, "ticket_images", default=[])
        ticket_amenities = self._safe_pop_field(validated_data, "ticket_amenities", default=[])
        ticket_included_services = self._safe_pop_field(validated_data, "ticket_included_services", default=[])
        ticket_itinerary = self._safe_pop_field(validated_data, "ticket_itinerary", default=[])
        ticket_hotel_meals = self._safe_pop_field(validated_data, "ticket_hotel_meals", default=[])
        transports = self._safe_pop_field(validated_data, "transports", default=[])
        tariffs = self._safe_pop_field(validated_data, "tariff", default=[])
        extra_service = self._safe_pop_field(validated_data, "extra_service", default=[])
        paid_extra_service = self._safe_pop_field(validated_data, "paid_extra_service", default=[])
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
        if extra_service:
            ExtraServicesModel.objects.bulk_create(
                [ExtraServicesModel(ticket=ticket, **meal) for meal in extra_service]
            )
        if paid_extra_service:
            PaidServicesModel.objects.bulk_create(
                [PaidServicesModel(ticket=ticket, **meal) for meal in paid_extra_service]
            )
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


class UpdateTicketsSerializer(BaseTicketsSerializer):
    ticket_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    ticket_amenities = TicketsAmenitiesWriteSerializer(many=True, write_only=True, required=False)
    ticket_included_services = TicketsIncludedServicesWriteSerializer(many=True, write_only=True, required=False)
    ticket_itinerary = TicketsItineraryWriteSerializer(many=True, write_only=True, required=False)
    ticket_hotel_meals = TicketsHotelMealsWriteSerializer(many=True, write_only=True, required=False)
    transports = FullTransportInfoWriteSerializer(many=True, write_only=True, required=False)
    tariff = FullTariffWriteSerializer(many=True, write_only=True, required=False)

    badge = serializers.ListField(
        child=serializers.IntegerField(),
        required=False,
        write_only=True
    )
    extra_service = ExtraServicesWriteSerializer(many=True, write_only=True, required=False)
    paid_extra_service = PaidExtraServicesWriteSerializer(many=True, write_only=True, required=False)

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
            "extra_service",
            "paid_extra_service",
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

    def update(self, instance, validated_data):
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
        )

        badge_data = self._safe_pop_field(validated_data, "badge", default=None)
        ticket_images = self._safe_pop_field(validated_data, "ticket_images", default=None)
        ticket_amenities = self._safe_pop_field(validated_data, "ticket_amenities", default=None)
        ticket_included_services = self._safe_pop_field(validated_data, "ticket_included_services", default=None)
        ticket_itinerary = self._safe_pop_field(validated_data, "ticket_itinerary", default=None)
        ticket_hotel_meals = self._safe_pop_field(validated_data, "ticket_hotel_meals", default=None)
        transports = self._safe_pop_field(validated_data, "transports", default=None)
        tariffs = self._safe_pop_field(validated_data, "tariff", default=None)
        extra_service = self._safe_pop_field(validated_data, "extra_service", default=None)
        paid_extra_service = self._safe_pop_field(validated_data, "paid_extra_service", default=None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if badge_data is not None:
            if badge_data:
                existing_badges = BadgeModel.objects.filter(id__in=badge_data)
                if existing_badges.exists():
                    instance.badge.set(existing_badges)
                else:
                    raise serializers.ValidationError({"badge": "Yuborilgan badge ID(lar) topilmadi yoki mavjud emas."})
            else:
                instance.badge.clear()

        if ticket_images is not None:
            instance.ticketimages.all().delete()
            if ticket_images:
                TicketsImagesModel.objects.bulk_create(
                    [TicketsImagesModel(image=image, ticket=instance) for image in ticket_images]
                )

        if ticket_amenities is not None:
            instance.ticketsamenities.all().delete()
            if ticket_amenities:
                TicketsAmenitiesModel.objects.bulk_create(
                    [TicketsAmenitiesModel(ticket=instance, **amenity) for amenity in ticket_amenities]
                )

        if ticket_included_services is not None:
            instance.ticketsincludedservices.all().delete()
            if ticket_included_services:
                TicketsIncludedServicesModel.objects.bulk_create(
                    [TicketsIncludedServicesModel(ticket=instance, **service) for service in ticket_included_services]
                )

        if ticket_hotel_meals is not None:
            instance.ticketshotelmeals.all().delete()
            if ticket_hotel_meals:
                TicketsHotelMealsModel.objects.bulk_create(
                    [TicketsHotelMealsModel(ticket=instance, **meal) for meal in ticket_hotel_meals]
                )

        if transports is not None:
            old_transports = instance.transports.all()
            instance.transports.clear()
            old_transports.delete()

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
                    instance.transports.set(full_transports)

        if tariffs is not None:
            old_tariffs = instance.tariff.all()
            instance.tariff.clear()
            old_tariffs.delete()

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
                    instance.tariff.set(full_tariffs)

        if extra_service is not None:
            instance.extraservices.all().delete()
            if extra_service:
                ExtraServicesModel.objects.bulk_create(
                    [ExtraServicesModel(ticket=instance, **meal) for meal in extra_service]
                )

        if paid_extra_service is not None:
            instance.paidservices.all().delete()
            if paid_extra_service:
                PaidServicesModel.objects.bulk_create(
                    [PaidServicesModel(ticket=instance, **meal) for meal in paid_extra_service]
                )

        if ticket_itinerary is not None:
            instance.ticketsitinerary.all().delete()

            for itinerary_data in ticket_itinerary:
                if not isinstance(itinerary_data, dict):
                    continue

                itinerary_images = itinerary_data.pop("ticket_itinerary_image", []) or []
                itinerary_destinations = itinerary_data.pop("ticket_itinerary_destinations", []) or []
                itinerary = TicketsItineraryModel.objects.create(ticket=instance, **itinerary_data)

                if itinerary_images:
                    TicketsItineraryImagesModel.objects.bulk_create(
                        [TicketsItineraryImagesModel(tickets_itinerary=itinerary, **img) for img in itinerary_images]
                    )

                if itinerary_destinations:
                    TicketsItineraryDestinationsModel.objects.bulk_create(
                        [TicketsItineraryDestinationsModel(tickets_itinerary=itinerary, **dest) for dest in
                         itinerary_destinations]
                    )

        return instance
