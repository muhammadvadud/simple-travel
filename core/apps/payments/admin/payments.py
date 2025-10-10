from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.payments.models import PaymentsModel


@admin.register(PaymentsModel)
class PaymentsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
