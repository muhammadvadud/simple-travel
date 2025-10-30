from django.db import models
from django.utils.translation import gettext_lazy as _


class AgencyReportPaymentChoices(models.TextChoices):
    """
    Agent Report Payment Choice
    """

    CLICK = "click", _("Click")
    PAYME = "payme", _("Payme")
