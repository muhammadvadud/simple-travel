from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.accounts.models.travel_agency import TravelAgency


@admin.register(TravelAgency)
class LikesAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
