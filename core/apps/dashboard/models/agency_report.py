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
    def create_report(cls, agency, order, total_income, payment_method):
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
            payment_method=payment_method,
        )

        agency.total_income += total_income
        agency.platform_income += platform_share
        agency.pending += agency_share
        agency.ticket_sold_count += 1
        agency.save(update_fields=["total_income", "platform_income", "pending", "ticket_sold_count"])

        ticket = report.order.ticket

        ticket.total_income += report.total_income
        ticket.sold_count += 1
        ticket.save(update_fields=["total_income", "sold_count"])

        user = order.user
        user.total_spent += total_income
        user.save(update_fields=["total_spent"])
        return report

    @classmethod
    def delete_report(cls, order):
        try:
            report = cls.objects.get(order=order)
        except cls.DoesNotExist:
            return False

        agency = report.travel_agency
        ticket = report.order.ticket
        user = report.order.user

        agency.total_income -= report.total_income
        agency.platform_income -= report.platform_share
        agency.pending -= report.agency_share
        agency.ticket_sold_count = max(0, agency.ticket_sold_count - 1)

        agency.total_income = max(0, agency.total_income)
        agency.platform_income = max(0, agency.platform_income)
        agency.pending = max(0, agency.pending)

        ticket.total_income -= report.total_income
        ticket.total_income = max(0, ticket.total_income)
        ticket.sold_count = max(0, ticket.sold_count - 1)
        ticket.save(update_fields=["total_income", "sold_count"])

        user.total_spent -= agency.total_income
        user.total_spent = max(0, user.total_spent)
        user.save(update_fields=["total_spent"])

        agency.save(update_fields=["total_income", "platform_income", "pending", "ticket_sold_count"])

        report.delete()
        return True
