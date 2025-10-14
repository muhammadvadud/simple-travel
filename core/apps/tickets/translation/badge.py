from modeltranslation.translator import TranslationOptions, register

from core.apps.tickets.models import BadgeModel


@register(BadgeModel)
class BadgeTranslation(TranslationOptions):
    fields = [
        "name"
    ]
