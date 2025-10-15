from rest_framework import permissions
from core.apps.tickets.models.tickets import TicketorderModel


class IsTicketBuyer(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action != 'create':
            return True

        ticket_id = request.data.get('ticket')
        user = request.user

        return TicketorderModel.objects.filter(
            user=user,
            ticket_id=ticket_id,
            order_status__in=["confirmed", "completed"]
        ).exists()
