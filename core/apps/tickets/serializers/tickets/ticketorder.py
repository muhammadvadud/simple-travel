from rest_framework import serializers

from core.apps.tickets.models import TicketorderModel


class BaseTicketorderSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketorderModel
        fields = [
            "id",
            "name",
        ]


class ListTicketorderSerializer(BaseTicketorderSerializer):
    class Meta(BaseTicketorderSerializer.Meta): ...


class RetrieveTicketorderSerializer(BaseTicketorderSerializer):
    class Meta(BaseTicketorderSerializer.Meta): ...


class CreateTicketorderSerializer(BaseTicketorderSerializer):
    class Meta(BaseTicketorderSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
