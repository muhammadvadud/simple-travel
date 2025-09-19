from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.tickets.models import TariffModel


@receiver(post_save, sender=TariffModel)
def TariffSignal(sender, instance, created, **kwargs): ...
