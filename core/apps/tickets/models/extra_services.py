from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from ..models.tickets import TicketsModel


class ExtraServicesModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    ticket = models.ForeignKey(TicketsModel, verbose_name=_("ticket"), related_name="ticket_extra_service",
                               on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            ticket=TicketsModel._create_fake(),
        )

    class Meta:
        db_table = "extra_services"
        verbose_name = _("ExtraServicesModel")
        verbose_name_plural = _("ExtraServicesModels")


class PaidServicesModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    price = models.IntegerField(verbose_name=_("price"))
    ticket = models.ForeignKey(TicketsModel, verbose_name=_("ticket"), related_name="ticket_extra_paid_service",
                               on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            price=40,
            ticket=TicketsModel._create_fake(),

        )

    class Meta:
        db_table = "paid_services"
        verbose_name = _("PaidServicesModel")
        verbose_name_plural = _("PaidServicesModels")
