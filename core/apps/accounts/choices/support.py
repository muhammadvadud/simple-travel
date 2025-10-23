from django.db import models
from django.utils.translation import gettext_lazy as _


class SupporStatusChoices(models.TextChoices):
    """
    Support Status Choice
    """

    PENDING = "pending", _("pending")
    DONE = "done", _("done")
    FAILED = "failed", _("failed")
