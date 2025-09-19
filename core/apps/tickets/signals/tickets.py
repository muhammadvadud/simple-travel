from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.tickets.models import TicketorderModel, TicketsModel


@receiver(post_save, sender=TicketsModel)
def TicketsSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=TicketorderModel)
def TicketorderSignal(sender, instance, created, **kwargs): ...
