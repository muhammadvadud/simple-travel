from modeltranslation.translator import TranslationOptions, register

from core.apps.tickets.models import TransportTicketModel


@register(TransportTicketModel)
class TransportTranslation(TranslationOptions):
    fields = [
        "name"
    ]
