from django_filters import rest_framework as filters

from core.apps.tickets.models import HotelModel, TicketsModel


class HotelFilter(filters.FilterSet):
    ticket = filters.ModelChoiceFilter(queryset=TicketsModel.objects.all())

    class Meta:
        model = HotelModel
        fields = [
            "ticket",
        ]
