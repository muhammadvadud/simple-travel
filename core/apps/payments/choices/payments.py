from django.db import models
from django.utils.translation import gettext_lazy as _


class PaymentStatusChoices(models.TextChoices):
    """
    Payments Status Choice
    """

    PENDING = "pending", _("Pending")
    SUCCESS = "success", _("Success")
    FAILED = "failed", _("Failed")
    CANCELLED = "cancelled", _("Cancelled")


class PaymentMethodChoices(models.TextChoices):
    """
    Payments Method Choice
    """

    CLICK = "click", _("Click")
    PAYME = "payme", _("Payme")
    OTHER = "other", _("Other")
