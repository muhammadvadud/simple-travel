from django_core.models.base import AbstractBaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Offerta(AbstractBaseModel):
    PERSON_TYPE_CHOICES = [
        ('individual', 'individual'),
        ('legal_entity', 'legal_entity'),
    ]

    title = models.CharField(max_length=255, verbose_name=_("title"))
    content = models.TextField(verbose_name=_("content"))
    person_type = models.CharField(max_length=255, choices=PERSON_TYPE_CHOICES, verbose_name=_("person type"),
                                   default='individual')
    is_active = models.BooleanField(verbose_name=_("is active"), default=False)

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'offerta'
        verbose_name = _("offerta")
        verbose_name_plural = _("offerta")
