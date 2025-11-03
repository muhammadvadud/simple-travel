from django.db import models
from django.utils.translation import gettext_lazy as _


class AgencyPayOutRequestChoices(models.TextChoices):
    """
    Agency PayOut Request Choices
    """
    
    PENDING = "pending", _("pending")
    APPROVED = "approved", _("approved")
    CANCELLED = "cancelled", _("cancelled")
