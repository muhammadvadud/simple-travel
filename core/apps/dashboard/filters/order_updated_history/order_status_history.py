from django_filters import rest_framework as filters

from core.apps.dashboard.models import OrderStatusHistoryModel


class OrderStatusHistoryFilter(filters.FilterSet):
    class Meta:
        model = OrderStatusHistoryModel
        fields = [
            "order",
        ]
