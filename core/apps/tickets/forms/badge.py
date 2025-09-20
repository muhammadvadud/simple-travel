from django import forms

from core.apps.tickets.models import BadgeModel


class BadgeForm(forms.ModelForm):

    class Meta:
        model = BadgeModel
        fields = "__all__"
