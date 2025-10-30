from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import SiteSettings, SiteSeo


@admin.register(SiteSettings)
class SiteSettingsAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(SiteSeo)
class SiteSeoAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
