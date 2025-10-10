from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from django.contrib.auth import get_user_model


class PaymentsModel(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("name"))

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "payments"
        verbose_name = _("PaymentsModel")
        verbose_name_plural = _("PaymentsModels")
