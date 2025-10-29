from django.db import models
from django.utils.translation import gettext_lazy as _


class BannerIdChoise(models.TextChoices):
    """
    Banner Id Choise
    """

    BANNER1 = "banner1", _("BANNER1")
    BANNER2 = "banner2", _("BANNER2")
    BANNER3 = "banner3", _("BANNER3")
    BANNER4 = "banner4", _("BANNER4")
