from django_filters import rest_framework as filters

from core.apps.tickets.models import HotelModel


class HotelFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = HotelModel
        fields = [
            "name",
        ]

