from django_core.models import AbstractBaseModel
from core.apps.accounts.models import TravelAgency
from django.db import models
from django.utils.translation import gettext_lazy as _
from ..choices.agency_payout_request import AgencyPayOutRequestChoices


class AgencyPayoutRequestModel(AbstractBaseModel):
    travel_agency = models.ForeignKey(TravelAgency, on_delete=models.CASCADE, verbose_name=_("Travel Agency"))
    amount = models.PositiveBigIntegerField(verbose_name=_("Amount"))
    status = models.CharField(max_length=255, choices=AgencyPayOutRequestChoices,
                              default=AgencyPayOutRequestChoices.PENDING,
                              verbose_name=_("Status"))

    class Meta:
        db_table = "agency_payout_request"
        verbose_name = _("Agentlik Pul chiqarish Arizasi")
        verbose_name_plural = _("Agentlik Pul chiqarish Arizasi")

    def __str__(self):
        return str(self.pk)
