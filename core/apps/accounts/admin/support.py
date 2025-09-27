from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.accounts.models import SupportModel


@admin.register(SupportModel)
class SupportAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
