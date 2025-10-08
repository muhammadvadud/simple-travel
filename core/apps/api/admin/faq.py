from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.api.models import FaqModel, FaqCategoryModel


@admin.register(FaqModel)
class FaqAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )

@admin.register(FaqCategoryModel)
class FaqCategoryAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
