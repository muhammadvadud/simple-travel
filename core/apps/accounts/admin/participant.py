from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.accounts.models import ParticipantModel, ParticipantPasportImageModel


class ParticipantPasportImageAdmin(admin.TabularInline):
    model = ParticipantPasportImageModel
    extra = 1


@admin.register(ParticipantModel)
class ParticipantAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
    inlines = [ParticipantPasportImageAdmin]
@admin.register(ParticipantPasportImageModel)
class ParticipantPasportImageModelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
