from modeltranslation.translator import TranslationOptions, register

from core.apps.tickets.models import Country, Region


@register(Country)
class CountryTranslation(TranslationOptions):
    fields = [
        "name"
    ]


@register(Region)
class RegionTranslation(TranslationOptions):
    fields = [
        "name"
    ]
