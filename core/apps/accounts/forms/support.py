from django import forms

from core.apps.accounts.models import SupportModel


class SupportForm(forms.ModelForm):

    class Meta:
        model = SupportModel
        fields = "__all__"
