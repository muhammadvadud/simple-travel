from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class TariffModel(AbstractBaseModel):
    Tariff_Choise = (
        ("3", "Standart"),
        ("4", "Comfort"),
        ("5", "Luxury"),
    )

    name = models.CharField(choices=Tariff_Choise, max_length=255, default=Tariff_Choise[0])

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
