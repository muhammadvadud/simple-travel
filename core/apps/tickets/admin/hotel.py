from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.tickets.models import HotelModel, HotelTypeModel,  HotelFeatureModel, \
    HotelFeatureTypeModel


@admin.register(HotelModel)
class HotelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(HotelTypeModel)
class HotelTypeModelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(HotelFeatureTypeModel)
class HotelFeatureTypeModelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )




@admin.register(HotelFeatureModel)
class HotelFeatureModelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
