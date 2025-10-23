from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from .travel_agency import TravelAgency
from ..choices.support import SupporStatusChoices


class SupportModel(AbstractBaseModel):
    travel_agency = models.ForeignKey(TravelAgency, related_name="support_agency", on_delete=models.CASCADE, null=True,
                                      blank=True)
    name = models.CharField(verbose_name=_("name"), max_length=255)
    phone_number = models.CharField(verbose_name=_("phone number"), max_length=255)
    status = models.CharField(verbose_name=_("status"), max_length=255, choices=SupporStatusChoices,
                              default=SupporStatusChoices.PENDING)
    created = models.DateTimeField(verbose_name=_("created"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("updated"), auto_now=True)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            phone_number="998940105669",
            travel_agency=TravelAgency._create_fake(),
        )

    class Meta:
        db_table = "support"
        verbose_name = _("SupportModel")
        verbose_name_plural = _("SupportModels")
