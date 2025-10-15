from rest_framework import serializers
from core.apps.tickets.models.tickets import TicketsCommentsModel

class CreateTicketComment(serializers.ModelSerializer):
    class Meta:
        model = TicketsCommentsModel
        fields = [
            "text",
            "rating",
            "ticket",
        ]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return TicketsCommentsModel.objects.create(**validated_data)
