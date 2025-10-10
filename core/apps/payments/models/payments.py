from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from django.contrib.auth import get_user_model


class PaymentsModel(AbstractBaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="payments_user")
    amount = models.PositiveBigIntegerField(verbose_name=_("amount"))
    currency = models.CharField(max_length=10, default="UZS")

    method = models.CharField(
        max_length=20,
        choices=PaymentMethod.choices,
        default=PaymentMethod.CLICK
    )

    status = models.CharField(
        max_length=20,
        choices=PaymentStatus.choices,
        default=PaymentStatus.PENDING
    )

    transaction_id = models.CharField(max_length=100, blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    extra_data = models.JSONField(blank=True, null=True)  # gateway response, etc.

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
