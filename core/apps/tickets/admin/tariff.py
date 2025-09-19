from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.tickets.models import TariffModel


@admin.register(TariffModel)
class TariffAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
