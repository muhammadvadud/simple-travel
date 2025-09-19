from django.db.models.signals import post_save
from django.dispatch import receiver

from core.apps.blog.models import CategoryModel, PostimagesModel, PostModel, TagModel


@receiver(post_save, sender=PostModel)
def PostSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=TagModel)
def TagSignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=CategoryModel)
def CategorySignal(sender, instance, created, **kwargs): ...


@receiver(post_save, sender=PostimagesModel)
def PostimagesSignal(sender, instance, created, **kwargs): ...
