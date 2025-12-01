from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.tickets.models import Country, Region


@admin.register(Country)
class CountryAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(Region)
class RegionAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
