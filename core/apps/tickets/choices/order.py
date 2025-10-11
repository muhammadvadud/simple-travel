from django.db import models
from django.utils.translation import gettext_lazy as _


class OrderStatusChoices(models.TextChoices):
    """
    Order Status Choices
    """

    PENDING_PAYMENT = "pending_payment", _("Pending Payment")
    PENDING_CONFIRMATION = "pending_confirmation", _("Pending Confirmation")
    CANCELLED = "cancelled", _("Cancelled")
    CONFIRMED = "confirmed", _("Confirmed")
    COMPLETED = "completed", _("Completed")
