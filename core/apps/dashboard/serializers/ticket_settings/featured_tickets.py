from rest_framework import serializers
from core.apps.tickets.models import TicketsModel


class UpdateFeaturedTicketSerializer(serializers.Serializer):
    def validate(self, attrs):
        ticket_id = self.context.get("ticket_id")
        value = self.context.get("value")

        ticket = TicketsModel.objects.filter(id=ticket_id).first()
        if not ticket:
            raise serializers.ValidationError("Ticket topilmadi.")

        featured_value = bool(value)
        if featured_value and not ticket.featured_tickets:
            count = TicketsModel.objects.filter(featured_tickets=True).count()
            if count >= 5:
                raise serializers.ValidationError(
                    "Faqat 5 ta ticket 'featured' bo‘lishi mumkin."
                )

        if value not in [0, 1]:
            raise serializers.ValidationError("Value faqat 0 yoki 1 bo‘lishi kerak.")

        attrs["ticket"] = ticket
        attrs["featured_value"] = featured_value
        return attrs

    def save(self):
        ticket = self.validated_data["ticket"]
        featured_value = self.validated_data["featured_value"]

        ticket.featured_tickets = featured_value
        ticket.save()

        return {
            "id": ticket.id,
            "featured_tickets": ticket.featured_tickets,
            "detail": f"Ticket 'featured_tickets' {featured_value} qilib o‘rnatildi."
        }
