from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Avg
from core.apps.tickets.models import TicketsCommentsModel


@receiver(post_save, sender=TicketsCommentsModel)
def update_ticket_rating(sender, instance, created, **kwargs):
    if created:
        ticket = instance.ticket
        avg_rating = TicketsCommentsModel.objects.filter(ticket=ticket).aggregate(avg=Avg("rating"))["avg"]
        ticket.rating = avg_rating or 0
        ticket.save(update_fields=["rating"])
