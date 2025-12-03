from django_filters import rest_framework as filters

from core.apps.tickets.models import Country


class CountryFilter(filters.FilterSet):
    class Meta:
        model = Country
        fields = [
            "name",
        ]
