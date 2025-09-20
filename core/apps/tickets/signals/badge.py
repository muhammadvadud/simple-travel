from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.tickets.models import BadgeModel


@receiver(post_save, sender=BadgeModel)
def BadgeSignal(sender, instance, created, **kwargs): ...
