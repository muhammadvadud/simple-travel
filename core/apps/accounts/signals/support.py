from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.accounts.models import SupportModel


@receiver(post_save, sender=SupportModel)
def SupportSignal(sender, instance, created, **kwargs): ...
