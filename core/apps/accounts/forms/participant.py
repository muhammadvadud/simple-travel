from django import forms

from core.apps.accounts.models import ParticipantModel


class ParticipantForm(forms.ModelForm):

    class Meta:
        model = ParticipantModel
        fields = "__all__"
