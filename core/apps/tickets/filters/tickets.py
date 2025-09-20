from django_filters import rest_framework as filters
from core.apps.tickets.models import TicketsModel


class TicketsFilter(filters.FilterSet):
    title = filters.CharFilter(field_name="title", lookup_expr="icontains")
    destinations = filters.CharFilter(field_name="ticket_itinerary__ticket_itinerary_destinations__name",
                                      lookup_expr="icontains")
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")
    cheapest = filters.BooleanFilter(method="filter_cheapest")
    most_expensive = filters.BooleanFilter(method="filter_most_expensive")
    visa_required = filters.BooleanFilter(method="filter_visa_required")
    duration_days = filters.NumberFilter(field_name="duration_days", lookup_expr="exact")
    hotel_rating = filters.NumberFilter(field_name="ticket_hotel__rating", lookup_expr="exact")
    meal_plan = filters.CharFilter(field_name="ticket_hotel__meal_plan", lookup_expr="icontains")
    hotel_type = filters.CharFilter(field_name="ticket_hotel__hotel_type__name", lookup_expr="icontains")
    ticket_amenities = filters.CharFilter(field_name="ticket_amenities__name", lookup_expr="icontains")

    class Meta:
        model = TicketsModel
        fields = [
            "title",
            "min_price",
            "max_price",
            "visa_required",
            "duration_days",
            "destinations",
            "hotel_rating",
            "hotel_type",
            "ticket_amenities",
        ]

    def filter_cheapest(self, queryset, name, value):
        if value:
            return queryset.order_by("price")
        return queryset

    def filter_most_expensive(self, queryset, name, value):
        if value:
            return queryset.order_by("-price")
        return queryset

    def filter_visa_required(self, queryset, name, value):
        if value:
            visa_required = queryset.filter(visa_required=value)
            return visa_required
        elif value is False:
            visa_required = queryset.filter(visa_required=value)
            return visa_required
        return queryset
