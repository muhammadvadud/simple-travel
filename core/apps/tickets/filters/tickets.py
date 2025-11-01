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
    hotel_rating = filters.NumberFilter(field_name="ticket_hotel__rating", lookup_expr="gte")
    rating = filters.NumberFilter(field_name="rating", lookup_expr="gte")
    meal_plan = filters.CharFilter(field_name="ticket_hotel__meal_plan", lookup_expr="icontains")
    hotel_type = filters.CharFilter(field_name="ticket_hotel__hotel_type__name", lookup_expr="icontains")
    ticket_amenities = filters.CharFilter(field_name="ticket_amenities__name", lookup_expr="icontains")
    departure = filters.CharFilter(field_name="departure", lookup_expr="icontains")
    destination = filters.CharFilter(field_name="destination", lookup_expr="icontains")
    min_departure_date = filters.DateFilter(field_name="departure_time", lookup_expr="gte")
    max_departure_date = filters.DateFilter(field_name="travel_time", lookup_expr="lte")
    passenger_count = filters.NumberFilter(field_name="passenger_count", lookup_expr="gte")
    hotel_name = filters.CharFilter(field_name="ticket_hotel__name", lookup_expr="icontains")
    hotel_feature = filters.CharFilter(method="filter_hotel_features")

    hotel_amenity = filters.CharFilter(
        method="filter_hotel_amenity"
    )

    class Meta:
        model = TicketsModel
        fields = [
            "title",
            "min_price",
            "max_price",
            "visa_required",
            "duration_days",
            "destinations",
            "rating",
            "hotel_type",
            "ticket_amenities",
            "departure",
            "destination",
            "departure_time",
            "travel_time",
            "min_departure_date",
            "max_departure_date",
            "passenger_count",
            "hotel_name",
            "featured_tickets",
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

    def filter_hotel_features(self, queryset, name, value_list):
        for feature in value_list:
            queryset = queryset.filter(
                ticket_hotel__hotel_features__feature_name__icontains=feature
            )
        return queryset.distinct()

    def filter_hotel_amenity(self, queryset, name, value):
        values = self.request.GET.getlist("hotel_amenity")
        if not values:
            return queryset

        for v in values:
            queryset = queryset.filter(
                ticket_hotel__hotel_amenities__name__iexact=v
            )
        return queryset.distinct()
