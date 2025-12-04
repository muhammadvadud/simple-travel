from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.tickets.models import (
    TicketorderModel,
    TicketsAmenitiesModel,
    TicketsCommentsModel,
    TicketsHotelMealsModel,
    TicketsImagesModel,
    TicketsIncludedServicesModel,
    TicketsItineraryDestinationsModel,
    TicketsItineraryImagesModel,
    TicketsItineraryModel,
    TicketsModel,
    TransportTicketModel,
    FullTransportInfoModel
)


class TicketsImagesInline(admin.TabularInline):
    model = TicketsImagesModel
    extra = 1


class TicketsIncludedServicesInline(admin.TabularInline):
    model = TicketsIncludedServicesModel
    extra = 1


class TicketsHotelMealsInline(admin.TabularInline):
    model = TicketsHotelMealsModel
    extra = 1


@admin.register(TicketsModel)
class TicketsAdmin(ModelAdmin):
    list_display = ("id", "title", "price", "departure_time", "destination", "passenger_count", "rating")
    inlines = [
        TicketsImagesInline,
        TicketsIncludedServicesInline,
        TicketsHotelMealsInline,
    ]


class TicketsItineraryImagesInline(admin.TabularInline):
    model = TicketsItineraryImagesModel
    extra = 1


class TicketsItineraryDestinationsInline(admin.TabularInline):
    model = TicketsItineraryDestinationsModel
    extra = 1


@admin.register(TicketsItineraryModel)
class TicketsItineraryAdmin(ModelAdmin):
    list_display = ("id", "ticket", "title", "duration")
    inlines = [TicketsItineraryImagesInline, TicketsItineraryDestinationsInline]


@admin.register(TicketsCommentsModel)
class TicketsCommentsAdmin(ModelAdmin):
    list_display = (
        "user",
        "text",
        "rating",
        "ticket",
    )


@admin.register(TicketorderModel)
class TicketorderAdmin(ModelAdmin):
    list_display = (
        "id",
        "ticket",
        "destination",
        "departure",
        "user",
    )


@admin.register(TransportTicketModel)
class TransportTicketModelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(FullTransportInfoModel)
class FullTransportInfoModelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(TicketsAmenitiesModel)
class TicketsAmenitiesModelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
