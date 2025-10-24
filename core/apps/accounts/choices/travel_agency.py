from django.db import models
from django.utils.translation import gettext_lazy as _


class TravelAgencyStatusChoices(models.TextChoices):
    """
    Travel Agency Status Choice
    """

    PENDING = "pending", _("pending")
    APPROVED = "approved", _("approved")
    CANCELLED = "cancelled", _("cancelled")
