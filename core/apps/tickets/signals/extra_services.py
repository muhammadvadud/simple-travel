from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.tickets.models import ExtraServicesModel, PaidServicesModel


@receiver(post_save, sender=ExtraServicesModel)
def ExtraServicesSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=PaidServicesModel)
def PaidServicesSignal(sender, instance, created, **kwargs): ...
