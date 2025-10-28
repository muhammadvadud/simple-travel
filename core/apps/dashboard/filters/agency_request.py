from django_filters import rest_framework as filters

from core.apps.accounts.models import TravelAgency


class TravelAgencyFilter(filters.FilterSet):
    class Meta:
        model = TravelAgency
        fields = [
            "status",
        ]
