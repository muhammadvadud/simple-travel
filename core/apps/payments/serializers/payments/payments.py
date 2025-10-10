from rest_framework import serializers

from core.apps.payments.models import PaymentsModel


class BasePaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentsModel
        fields = [
            "id",
            "name",
        ]


class ListPaymentsSerializer(BasePaymentsSerializer):
    class Meta(BasePaymentsSerializer.Meta): ...


class RetrievePaymentsSerializer(BasePaymentsSerializer):
    class Meta(BasePaymentsSerializer.Meta): ...


class CreatePaymentsSerializer(BasePaymentsSerializer):
    class Meta(BasePaymentsSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
