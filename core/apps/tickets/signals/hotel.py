from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.tickets.models import HotelModel


@receiver(post_save, sender=HotelModel)
def HotelSignal(sender, instance, created, **kwargs): ...
