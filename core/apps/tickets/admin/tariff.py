from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.tickets.models import TariffModel, FullTariff


@admin.register(TariffModel)
class TariffAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(FullTariff)
class FullTariffAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
