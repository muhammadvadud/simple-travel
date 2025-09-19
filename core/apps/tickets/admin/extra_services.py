from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.tickets.models import ExtraServicesModel, PaidServicesModel


@admin.register(ExtraServicesModel)
class ExtraServocesAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )





@admin.register(PaidServicesModel)
class PaidServicesAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
