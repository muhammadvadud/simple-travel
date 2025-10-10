from django_filters import rest_framework as filters

from core.apps.payments.models import PaymentsModel


class PaymentsFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = PaymentsModel
        fields = [
            "name",
        ]
