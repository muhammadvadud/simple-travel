from django import forms

from core.apps.tickets.models import PaidServicesModel


class PaidServicesForm(forms.ModelForm):

    class Meta:
        model = PaidServicesModel
        fields = "__all__"
