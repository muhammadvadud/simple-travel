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


class FullTariff(AbstractBaseModel):
    tariff = models.ForeignKey(TariffModel, on_delete=models.PROTECT, verbose_name=_("tariff"), related_name="price")
    price = models.PositiveBigIntegerField(verbose_name=_("price"), default=0)

    def __str__(self):
        return str(self.id)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "tariff_price"
        verbose_name = _("FullTariff")
        verbose_name_plural = _("FullTariffs")
