from modeltranslation.translator import TranslationOptions, register

from core.apps.dashboard.models import SiteSeo


@register(SiteSeo)
class SiteSeoTranslation(TranslationOptions):
    fields = [
        "title",
        "description",
        "keywords",
        "og_title",
        "og_description",
    ]
