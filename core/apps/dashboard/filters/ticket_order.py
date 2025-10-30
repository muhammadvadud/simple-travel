from django_filters import rest_framework as filters

from core.apps.tickets.models import TicketorderModel


class TicketOrderFilter(filters.FilterSet):
    class Meta:
        model = TicketorderModel
        fields = [
            "order_status",
        ]
