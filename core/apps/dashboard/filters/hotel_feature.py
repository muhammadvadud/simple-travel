from django_filters import rest_framework as filters

from core.apps.tickets.models import HotelFeatureModel


class HotelFeatureFilter(filters.FilterSet):
    feature_type = filters.NumberFilter(field_name="feature_type__id")

    class Meta:
        model = HotelFeatureModel
        fields = [
            "feature_type",
        ]
