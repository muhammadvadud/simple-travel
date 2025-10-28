from django_filters import rest_framework as filters

from core.apps.accounts.models import SupportModel


class SupportFilter(filters.FilterSet):

    class Meta:
        model = SupportModel
        fields = [
            "status",
        ]
