from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.accounts.models import ParticipantModel


@admin.register(ParticipantModel)
class ParticipantAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
