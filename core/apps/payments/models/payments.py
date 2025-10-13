from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from django.contrib.auth import get_user_model
from ..choices.payments import PaymentMethodChoices, PaymentStatusChoices
from core.apps.accounts.models import User


class PaymentsModel(AbstractBaseModel):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="payments_user")
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    ########
    # Bu yoki qoladi yoki olib tashlanadi!
    currency = models.CharField(max_length=10, default="UZS")
    ########
    method = models.CharField(
        max_length=20,
        choices=PaymentMethodChoices,
        default=PaymentMethodChoices.OTHER
    )

    status = models.CharField(
        max_length=20,
        choices=PaymentStatusChoices,
        default=PaymentStatusChoices.CANCELLED
    )

    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.CharField(max_length=100, blank=True, null=True)

    description = models.TextField(blank=True, null=True)
    extra_data = models.JSONField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            user=User._create_fake(),
            amount=12312312.00,
            currency="mock",
            status=PaymentStatusChoices.SUCCESS,
            transaction_id="ID:1234",
        )

    class Meta:
        db_table = "payments"
        verbose_name = _("PaymentsModel")
        verbose_name_plural = _("PaymentsModels")
