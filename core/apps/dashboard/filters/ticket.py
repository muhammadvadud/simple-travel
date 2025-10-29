from django_filters import rest_framework as filters

from core.apps.tickets.models import TicketsModel


class TicketFilter(filters.FilterSet):
    class Meta:
        model = TicketsModel
        fields = [
            "featured_tickets",
        ]
