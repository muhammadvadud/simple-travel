from django_core.models import AbstractBaseModel
from django.db import models
from django.contrib.auth import get_user_model
from core.apps.tickets.models import TicketorderModel
from core.apps.tickets.choices import OrderStatusChoices
from django.utils.translation import gettext_lazy as _


class OrderStatusHistoryModel(AbstractBaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    order = models.ForeignKey(TicketorderModel, on_delete=models.CASCADE)
    old_status = models.CharField(max_length=255, choices=OrderStatusChoices)
    new_status = models.CharField(max_length=255, choices=OrderStatusChoices)

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'order_status_history'
        verbose_name = _("OrderStatusHistory")
        verbose_name_plural = _("OrderStatusHistorys")
