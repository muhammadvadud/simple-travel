from django.contrib import admin
from unfold.admin import ModelAdmin

from ..models import OrderStatusHistoryModel


@admin.register(OrderStatusHistoryModel)
class OrderStatusHistoryModelAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
