from django.db import models
from django.utils.translation import gettext_lazy as _
from ..choices.agency_report import AgencyReportPaymentChoices


class AgencyReport(models.Model):
    travel_agency = models.ForeignKey(
        "accounts.TravelAgency",
        on_delete=models.CASCADE,
        related_name="reports",
        verbose_name=_("Travel agency"),
    )
    order = models.ForeignKey(
        "tickets.TicketorderModel",
        on_delete=models.CASCADE,
        related_name="agency_reports",
        verbose_name=_("Order"),
        help_text=_("Hisobot qaysi buyurtmaga tegishli ekanligini ko‘rsatadi."),
    )
    payment_method = models.CharField(
        max_length=50,
        choices=AgencyReportPaymentChoices,
        default=AgencyReportPaymentChoices.CLICK,
        verbose_name=_("To‘lov tizimi")
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

    def __str__(self):
        return f"{self.travel_agency.name} — {self.total_income} so‘m ({self.created_at:%Y-%m-%d})"

    @classmethod
    def create_report(cls, agency, order, total_income):
        """
        To‘lov muvaffaqiyatli yakunlanganda hisobot yaratish.
        """
        percentage = agency.share_percentage
        platform_share = total_income * percentage // 100
        agency_share = total_income - platform_share

        report = cls.objects.create(
            travel_agency=agency,
            order=order,
            total_income=total_income,
            platform_share=platform_share,
            agency_share=agency_share,
            percentage_at_time=percentage,
        )

        agency.total_income += total_income
        agency.platform_income += platform_share
        agency.pending += agency_share
        agency.save(update_fields=["total_income", "platform_income", "pending"])

        return report

    @classmethod
    def delete_report(cls, order):
        """
        To‘lov bekor qilinsa, order bo‘yicha hisobotni o‘chirish.
        """
        try:
            report = cls.objects.get(order=order)
        except cls.DoesNotExist:
            return None

        agency = report.travel_agency

        agency.total_income -= report.total_income
        agency.platform_income -= report.platform_share
        agency.pending -= report.agency_share

        agency.total_income = max(0, agency.total_income)
        agency.platform_income = max(0, agency.platform_income)
        agency.pending = max(0, agency.pending)

        agency.save(update_fields=["total_income", "platform_income", "pending"])

        report.delete()
        return True
