from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
