from django.db import models
from django.utils.translation import gettext_lazy as _


class TariffChoices(models.TextChoices):
    """
    Tariff Choice
    """

    Standart = "standart", _("3 - Standart")
    Comfort = "comfort", _("4 - Comfort")
    Luxury = "luxury", _("5 - Luxury")
