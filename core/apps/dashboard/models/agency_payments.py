from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_core.models.base import AbstractBaseModel


class TravelAgencyPaymentModel(AbstractBaseModel):
    travel_agency = models.ForeignKey(
        "accounts.TravelAgency",
        on_delete=models.CASCADE,
        related_name="payments",
        verbose_name=_("Agentlik")
    )
    amount = models.PositiveBigIntegerField(verbose_name=_("O‘tkazilgan summa"))
    note = models.TextField(
        blank=True,
        null=True,
        verbose_name=_("Izoh (ixtiyoriy)")
    )
    accountant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="agency_payments",
        verbose_name=_("Buxgalter")
    )

    class Meta:
        verbose_name = _("Agentlik to‘lovi")
        verbose_name_plural = _("Agentlik to‘lovlari")
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.travel_agency.name} — {self.amount} so‘m"
