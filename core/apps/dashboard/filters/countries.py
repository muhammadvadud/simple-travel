from django_filters import rest_framework as filters

from core.apps.tickets.models import Region, Country


class RegionFilter(filters.FilterSet):
    country = filters.ModelChoiceFilter(queryset=Country.objects.all(), field_name="country")
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Region
        fields = [
            "country",
            "name",
        ]


class CountryFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Country
        fields = [
            "name",
        ]
