from modeltranslation.translator import TranslationOptions, register

from core.apps.tickets.models import HotelModel


@register(HotelModel)
class HotelTranslation(TranslationOptions):
    fields = []
