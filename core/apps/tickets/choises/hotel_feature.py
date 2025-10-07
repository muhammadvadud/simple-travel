from django.db import models
from django.utils.translation import gettext_lazy as _


class HotelFeature(models.TextChoices):
    """
    Hotel Feature Choice
    """

    CHILDREN_SECTION = "children_section", _("Bolalar bo‘limi")
    BEACH = "beach", _("Plyaj")
    POOL = "pool", _("Basseyn")
