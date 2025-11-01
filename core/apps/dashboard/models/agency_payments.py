from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django_core.models.base import AbstractBaseModel
from django.db import transaction
from rest_framework.exceptions import ValidationError


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

    @transaction.atomic
    def create_report(self):
        """Model yaratilganda agentlikning balansini yangilaydi"""
        agency = self.travel_agency
        if not agency:
            return

        if (agency.pending or 0) < self.amount:
            raise ValidationError(
                {"amount": _("To‘lov summasi agentlikning mavjud 'pending' balansidan katta bo‘lishi mumkin emas.")}
            )

        agency.pending = (agency.pending or 0) - self.amount
        agency.paid = (agency.paid or 0) + self.amount
        agency.save(update_fields=["pending", "paid"])

    @transaction.atomic
    def delete_report(self):
        """To‘lov o‘chirilganda balansni teskari hisoblaydi"""
        agency = self.travel_agency
        if not agency:
            return

        agency.pending = (agency.pending or 0) + self.amount
        agency.paid = (agency.paid or 0) - self.amount
        agency.save(update_fields=["pending", "paid"])

    def save(self, *args, **kwargs):
        """Model yaratilganda avtomatik hisobot yaratish"""
        is_new = self._state.adding
        super().save(*args, **kwargs)
        if is_new:
            self.create_report()

    def delete(self, *args, **kwargs):
        """Model o‘chirilganda avtomatik hisobotni teskari qilish"""
        self.delete_report()
        super().delete(*args, **kwargs)
