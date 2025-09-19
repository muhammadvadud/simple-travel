from django_filters import rest_framework as filters

from core.apps.tickets.models import TariffModel


class TariffFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = TariffModel
        fields = [
            "name",
        ]
