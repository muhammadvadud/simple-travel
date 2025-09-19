from django import forms

from core.apps.tickets.models import ExtraServicesModel, PaidServicesModel


class ExtraServicesForm(forms.ModelForm):

    class Meta:
        model = ExtraServicesModel
        fields = "__all__"


class PaidServicesForm(forms.ModelForm):

    class Meta:
        model = PaidServicesModel
        fields = "__all__"
