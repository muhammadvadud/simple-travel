from django_filters import rest_framework as filters

from core.apps.dashboard.models import AgencyPayoutRequestModel


class AgencyPayoutRequestFilter(filters.FilterSet):
    class Meta:
        model = AgencyPayoutRequestModel
        fields = [
            "status",
        ]
