from django_filters import rest_framework as filters

from core.apps.api.models import BannerModel


class BannerFilter(filters.FilterSet):
    class Meta:
        model = BannerModel
        fields = [
            "position",
        ]
