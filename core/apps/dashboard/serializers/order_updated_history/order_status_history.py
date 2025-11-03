from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.apps.dashboard.models import OrderStatusHistoryModel
from core.apps.tickets.models import TicketorderModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "role",
        ]


class BaseOrderStatusHistorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = OrderStatusHistoryModel
        fields = [
            "id",
            "user",
            "order",
            "old_status",
            "new_status",
        ]


class ListOrderStatusHistorySerializer(BaseOrderStatusHistorySerializer):
    class Meta(BaseOrderStatusHistorySerializer.Meta): ...


class RetrieveOrderStatusHistorySerializer(BaseOrderStatusHistorySerializer):
    class Meta(BaseOrderStatusHistorySerializer.Meta): ...


class CreateOrderStatusHistorySerializer(BaseOrderStatusHistorySerializer):
    order = serializers.PrimaryKeyRelatedField(queryset=TicketorderModel.objects.all())

    class Meta(BaseOrderStatusHistorySerializer.Meta):
        fields = [
            "id",
            "user",
            "order",
            "old_status",
            "new_status",
        ]

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        history = OrderStatusHistoryModel.objects.create(**validated_data)
        return history
