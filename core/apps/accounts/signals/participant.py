from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.accounts.models import ParticipantModel


@receiver(post_save, sender=ParticipantModel)
def ParticipantSignal(sender, instance, created, **kwargs): ...
