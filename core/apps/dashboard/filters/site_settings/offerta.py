from django_filters import rest_framework as filters

from core.apps.dashboard.models import Offerta


class OffertaFilter(filters.FilterSet):
    class Meta:
        model = Offerta
        fields = [
            "person_type",
        ]
