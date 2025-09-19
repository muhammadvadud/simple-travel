from django import forms

from core.apps.tickets.models import TariffModel


class TariffForm(forms.ModelForm):

    class Meta:
        model = TariffModel
        fields = "__all__"
