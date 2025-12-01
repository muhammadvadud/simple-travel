from django_filters import rest_framework as filters

from core.apps.tickets.models import Region, Country


class RegionFilter(filters.FilterSet):
    country = filters.ModelChoiceFilter(queryset=Country.objects.all(), field_name="country")

    class Meta:
        model = Region
        fields = [
            "country",
        ]
