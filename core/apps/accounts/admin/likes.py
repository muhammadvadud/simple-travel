from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.accounts.models import LikesModel


@admin.register(LikesModel)
class LikesAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
