from modeltranslation.translator import TranslationOptions, register

from core.apps.tickets.models import ExtraServicesModel, PaidServicesModel


@register(ExtraServicesModel)
class ExtraServicesTranslation(TranslationOptions):
    fields = []


@register(PaidServicesModel)
class PaidServicesTranslation(TranslationOptions):
    fields = []
