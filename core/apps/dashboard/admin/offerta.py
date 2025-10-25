from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import Offerta


@admin.register(Offerta)
class OffertaAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
