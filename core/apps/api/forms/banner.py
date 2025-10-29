from django import forms

from core.apps.api.models import BannerModel


class BannerForm(forms.ModelForm):

    class Meta:
        model = BannerModel
        fields = "__all__"
