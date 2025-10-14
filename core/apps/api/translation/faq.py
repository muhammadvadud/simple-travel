from modeltranslation.translator import TranslationOptions, register

from core.apps.api.models import FaqModel, FaqCategoryModel


@register(FaqModel)
class FaqTranslation(TranslationOptions):
    fields = [
        "title",
        "text",
    ]


@register(FaqCategoryModel)
class FaqCategoryModelTranslation(TranslationOptions):
    fields = [
        "name",
    ]
