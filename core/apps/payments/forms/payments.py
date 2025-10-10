from django import forms

from core.apps.payments.models import PaymentsModel


class PaymentsForm(forms.ModelForm):

    class Meta:
        model = PaymentsModel
        fields = "__all__"
