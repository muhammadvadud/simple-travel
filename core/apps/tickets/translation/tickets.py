from modeltranslation.translator import TranslationOptions, register

from core.apps.tickets.models import TicketorderModel, TicketsModel


@register(TicketsModel)
class TicketsTranslation(TranslationOptions):
    fields = []


@register(TicketorderModel)
class TicketorderTranslation(TranslationOptions):
    fields = []
