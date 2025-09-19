from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.accounts.models import LikesModel


@receiver(post_save, sender=LikesModel)
def LikesSignal(sender, instance, created, **kwargs): ...
