from django_filters import rest_framework as filters

from core.apps.accounts.models import TravelAgency


class TravelAgencyFilter(filters.FilterSet):
    category = filters.CharFilter(field_name="category", lookup_expr="icontains")

    class Meta:
        model = TravelAgency
        fields = [
            "status",
        ]
