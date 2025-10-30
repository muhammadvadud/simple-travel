from modeltranslation.translator import TranslationOptions, register

from core.apps.dashboard.models import Offerta


@register(Offerta)
class OffertaTranslation(TranslationOptions):
    fields = [
        "title",
        "content",
    ]
