from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import AgencyReport


@admin.register(AgencyReport)
class AgencyReportAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
