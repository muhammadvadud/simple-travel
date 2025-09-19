from django_filters import rest_framework as filters

from core.apps.tickets.models import TicketorderModel, TicketsModel


class TicketsFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = TicketsModel
        fields = [
            "name",
        ]


class TicketorderFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = TicketorderModel
        fields = [
            "name",
        ]
