from modeltranslation.translator import TranslationOptions, register

from core.apps.dashboard.models import HelpPage


@register(HelpPage)
class HelpPageTranslation(TranslationOptions):
    fields = [
        "title",
        "content",
    ]
