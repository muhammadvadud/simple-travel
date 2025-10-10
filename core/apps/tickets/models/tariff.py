from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from ..choices.tariff import TariffChoices


class TariffModel(AbstractBaseModel):
    name = models.CharField(choices=TariffChoices, max_length=255, default=TariffChoices.Standart)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "tariff"
        verbose_name = _("TariffModel")
        verbose_name_plural = _("TariffModels")
