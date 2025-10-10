from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.payments.models import PaymentsModel


@receiver(post_save, sender=PaymentsModel)
def PaymentsSignal(sender, instance, created, **kwargs): ...
