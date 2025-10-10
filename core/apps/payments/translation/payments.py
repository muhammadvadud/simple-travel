from modeltranslation.translator import TranslationOptions, register

from core.apps.payments.models import PaymentsModel


@register(PaymentsModel)
class PaymentsTranslation(TranslationOptions):
    fields = []
