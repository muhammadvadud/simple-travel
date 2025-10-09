from django.db import models
from django.utils.translation import gettext_lazy as _


class ParticipantGenderChoices(models.TextChoices):
    """
    Participant Gender Choice
    """

    Male = "male", _("Male")
    Female = "female", _("Female")
