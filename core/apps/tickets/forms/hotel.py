from django import forms

from core.apps.tickets.models import HotelModel


class HotelForm(forms.ModelForm):

    class Meta:
        model = HotelModel
        fields = "__all__"
