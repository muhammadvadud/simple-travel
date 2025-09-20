from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.tickets.models import BadgeModel


@admin.register(BadgeModel)
class BadgeAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
