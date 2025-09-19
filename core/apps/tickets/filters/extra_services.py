from django_filters import rest_framework as filters

from core.apps.tickets.models import ExtraServicesModel, PaidServicesModel


class ExtraServicesFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ExtraServicesModel
        fields = [
            "name",
        ]


class PaidServicesFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = PaidServicesModel
        fields = [
            "name",
        ]
