from django_core.models.base import AbstractBaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class HelpPage(AbstractBaseModel):
    PAGE_TYPE_CHOICES = [
        ('privacy_policy', 'Maxfiylik siyosati'),
        ('user_agreement', 'Foydalanuvchi qo\'llanmasi'),
    ]

    title = models.CharField(max_length=255, verbose_name=_("title"))
    content = models.TextField(verbose_name=_("content"))
    page_type = models.CharField(max_length=255, choices=PAGE_TYPE_CHOICES, verbose_name=_("person type"),
                                 default='privacy_policy')
    is_active = models.BooleanField(verbose_name=_("is active"), default=False)

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'help_page'
        verbose_name = _("help page")
        verbose_name_plural = _("help pages")
