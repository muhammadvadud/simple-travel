from django.db import models
from django.utils.translation import gettext_lazy as _


class RoleChoice(models.TextChoices):
    """
    User Role Choice
    """

    SUPERUSER = "superuser", _("Superuser")
    ADMIN = "admin", _("Admin")
    Moderator = "moderator", _("Moderator")
    TourAdmin = "tour_admin", _("TourAdmin")
    USER = "user", _("User")
