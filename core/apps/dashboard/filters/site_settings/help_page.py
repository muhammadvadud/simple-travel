from django_filters import rest_framework as filters

from core.apps.dashboard.models import HelpPage


class HelpPageFilter(filters.FilterSet):
    class Meta:
        model = HelpPage
        fields = [
            "page_type",
        ]
