from modeltranslation.translator import TranslationOptions, register

from core.apps.accounts.models import ParticipantModel


@register(ParticipantModel)
class ParticipantTranslation(TranslationOptions):
    fields = []
