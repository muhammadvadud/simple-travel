from django_filters import rest_framework as filters

from core.apps.tickets.models import HotelModel, TicketsModel, HotelMealPlan


class HotelFilter(filters.FilterSet):
    ticket = filters.ModelChoiceFilter(queryset=TicketsModel.objects.all())

    class Meta:
        model = HotelModel
        fields = [
            "ticket",
        ]


class HotelMealPlanFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = HotelMealPlan
        fields = [
            "name",
        ]
