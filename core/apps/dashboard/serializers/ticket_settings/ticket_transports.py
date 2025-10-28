from rest_framework import serializers
from core.apps.tickets.models import TransportTicketModel


class BaseTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransportTicketModel
        fields = [
            "id",
            "name",
            "icon_name",
        ]


class ListTransportSerializer(BaseTransportSerializer):
    class Meta(BaseTransportSerializer.Meta): ...


class RetrieveTransportSerializer(BaseTransportSerializer):
    class Meta(BaseTransportSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
            "icon_name",
        ]


class CreateTransportSerializer(BaseTransportSerializer):
    class Meta(BaseTransportSerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
            "icon_name",
        ]
