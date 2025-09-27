from django_filters import rest_framework as filters

from core.apps.accounts.models import SupportModel


class SupportFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = SupportModel
        fields = [
            "name",
        ]
