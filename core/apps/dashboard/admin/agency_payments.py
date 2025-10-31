from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import TravelAgencyPaymentModel


@admin.register(TravelAgencyPaymentModel)
class TravelAgencyPaymentModelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
