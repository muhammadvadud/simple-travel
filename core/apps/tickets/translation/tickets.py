from modeltranslation.translator import TranslationOptions, register

from core.apps.tickets.models import TicketorderModel, TicketsModel, TicketsAmenitiesModel, \
    TicketsIncludedServicesModel, TicketsItineraryModel, TicketsItineraryDestinationsModel, TicketsHotelMealsModel


@register(TicketsModel)
class TicketsTranslation(TranslationOptions):
    fields = [
        "title",
        "location_name",
        "hotel_info",
        "hotel_meals",
    ]


@register(TicketorderModel)
class TicketorderTranslation(TranslationOptions):
    fields = [
        "departure",
        "destination",
    ]


@register(TicketsAmenitiesModel)
class TicketsAmenitiesModelTranslation(TranslationOptions):
    fields = [
        "name"
    ]


@register(TicketsIncludedServicesModel)
class TicketsIncludedServicesModelTranslation(TranslationOptions):
    fields = [
        "title",
        "desc",
    ]


@register(TicketsItineraryModel)
class TicketsItineraryModelTranslation(TranslationOptions):
    fields = [
        "title",
    ]


@register(TicketsItineraryDestinationsModel)
class TicketsItineraryDestinationsModelTranslation(TranslationOptions):
    fields = [
        "name",
    ]


@register(TicketsHotelMealsModel)
class TicketsHotelMealsModelTranslation(TranslationOptions):
    fields = [
        "name",
        "desc",
    ]
