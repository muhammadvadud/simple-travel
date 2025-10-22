from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class BadgeModel(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("badge name"))
    color = models.CharField(max_length=255, verbose_name=_("badge color"), default="#FFFFFF")

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "badge"
        verbose_name = _("BadgeModel")
        verbose_name_plural = _("BadgeModels")
