from django_filters import rest_framework as filters

from core.apps.accounts.models import ParticipantModel


class ParticipantFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = ParticipantModel
        fields = [
            "name",
        ]
