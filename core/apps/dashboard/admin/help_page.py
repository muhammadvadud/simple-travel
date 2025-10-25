from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import HelpPage


@admin.register(HelpPage)
class HelpPageAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
