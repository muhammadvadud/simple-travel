from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.tickets.models import HotelModel, HotelImagesModel, HotelTypeModel


class HotelImagesInline(admin.TabularInline):
    model = HotelImagesModel
    extra = 1


@admin.register(HotelModel)
class HotelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    inlines = (
        HotelImagesInline,
    )


@admin.register(HotelTypeModel)
class HotelTypeModelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
