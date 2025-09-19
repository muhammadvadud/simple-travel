from django import forms

from core.apps.tickets.models import TicketorderModel, TicketsModel


class TicketsForm(forms.ModelForm):

    class Meta:
        model = TicketsModel
        fields = "__all__"


class TicketorderForm(forms.ModelForm):

    class Meta:
        model = TicketorderModel
        fields = "__all__"
