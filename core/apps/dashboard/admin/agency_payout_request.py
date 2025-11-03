from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import AgencyPayoutRequestModel


@admin.register(AgencyPayoutRequestModel)
class AgencyPayoutRequestModelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
