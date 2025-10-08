from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import FaqModel


@register(FaqModel)
class FaqTranslation(TranslationOptions):
    fields = []
