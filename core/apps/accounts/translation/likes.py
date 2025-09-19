from modeltranslation.translator import TranslationOptions, register

from core.apps.accounts.models import LikesModel


@register(LikesModel)
class LikesTranslation(TranslationOptions):
    fields = []
