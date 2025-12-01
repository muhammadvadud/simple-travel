from django.db import models
from django_core.models.base import AbstractBaseModel
from django.utils.translation import gettext_lazy as _


class Country(AbstractBaseModel):
    name = models.CharField(verbose_name=_("Country Name"), max_length=255)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = "countries"
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")


class Region(AbstractBaseModel):
    country = models.ForeignKey(Country, related_name="regions", on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_("Region Name"), max_length=255)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            country=Country._create_fake(),
        )

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = "regions"
        verbose_name = _("Region")
        verbose_name_plural = _("Regions")
