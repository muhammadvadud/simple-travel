from rest_framework import serializers
from django.shortcuts import get_object_or_404
from core.apps.tickets.models.tickets import TicketorderModel
from core.utils.get_payments_url import get_click_url, get_payme_url


class PaymentSerializer(serializers.Serializer):
    return_url = serializers.CharField(write_only=True, required=True)
    order_id = serializers.CharField(write_only=True, required=True)
    url = serializers.SerializerMethodField()

    def get_url(self, obj):

        payment_type = self.context.get("payment_type") or \
                       (self.context.get("request").query_params.get("payment_type") if self.context.get(
                           "request") else None)

        order_id = obj.get("order_id")
        return_url = obj.get("return_url")

        if not payment_type:
            raise serializers.ValidationError("Payment type is required")

        if not return_url:
            raise serializers.ValidationError({"return_url": "Return URL is required."})

        order = get_object_or_404(TicketorderModel, id=order_id)

        amount = order.total_price

        if payment_type == "click":
            return get_click_url(
                order_id=order.id,
                amount=amount,
                return_url=return_url,
            )
        elif payment_type == "payme":
            return get_payme_url(
                order_id=order.id,
                amount=amount,
                return_url=return_url,
            )

        raise serializers.ValidationError("Unsupported payment type.")
