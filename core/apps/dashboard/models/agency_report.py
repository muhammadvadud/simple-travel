from django.db import models
from django.utils.translation import gettext_lazy as _


class AgencyReport(models.Model):
    travel_agency = models.ForeignKey(
        "accounts.TravelAgency",
        on_delete=models.CASCADE,
        related_name="reports",
        verbose_name=_("Travel agency")
    )

    total_income = models.PositiveBigIntegerField(verbose_name=_("Umumiy tushum"))
    platform_share = models.PositiveBigIntegerField(verbose_name=_("Platforma ulushi"))
    agency_share = models.PositiveBigIntegerField(verbose_name=_("Agentlik ulushi"))
    percentage_at_time = models.PositiveIntegerField(verbose_name=_("Hisobot vaqtidagi foiz"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Yaratilgan vaqt"))

    class Meta:
        verbose_name = _("Agentlik hisobot")
        verbose_name_plural = _("Agentlik hisobotlari")
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["travel_agency"]),
            models.Index(fields=["created_at"]),
        ]

    def __str__(self):
        return f"{self.travel_agency.name} — {self.created_at.strftime('%Y-%m-%d')}"

    @classmethod
    def create_report(cls, agency, total_income):
        """Yangi hisobot yaratish uchun yordamchi funksiya"""
        percentage = agency.share_percentage
        platform_share = total_income * percentage // 100
        agency_share = total_income - platform_share

        report = cls.objects.create(
            travel_agency=agency,
            total_income=total_income,
            platform_share=platform_share,
            agency_share=agency_share,
            percentage_at_time=percentage,
        )

        agency.total_income += total_income
        agency.paid += agency_share
        agency.save(update_fields=["total_income", "paid"])

        return report
