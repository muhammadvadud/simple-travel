from modeltranslation.translator import TranslationOptions, register

from core.apps.tickets.models import TariffModel


@register(TariffModel)
class TariffTranslation(TranslationOptions):
    fields = [
        "name"
    ]
