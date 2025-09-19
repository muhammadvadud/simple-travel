from django import forms

from core.apps.accounts.models import LikesModel


class LikesForm(forms.ModelForm):

    class Meta:
        model = LikesModel
        fields = "__all__"
