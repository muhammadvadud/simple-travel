from core.apps.tickets.models import TicketsModel as Ticket


def get_locations_by_language(lang: str) -> dict:
    departure_field = f"departure_{lang}"
    destination_field = f"destination_{lang}"

    departures = Ticket.objects.values_list(departure_field, flat=True)
    destinations = Ticket.objects.values_list(destination_field, flat=True)

    unique_departures = sorted({d for d in departures if d})
    unique_destinations = sorted({d for d in destinations if d})

    return {
        "departures": unique_departures,
        "destinations": unique_destinations,
    }
