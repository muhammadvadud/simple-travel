from rest_framework import serializers, status
from core.apps.tickets.serializers.tickets.tickets import ListTicketsSerializer
from core.apps.accounts.models import LikesModel
from core.apps.tickets.models import TicketsModel


class BaseLikesSerializer(serializers.ModelSerializer):
    ticket = ListTicketsSerializer(read_only=True)

    class Meta:
        model = LikesModel
        fields = [
            "id",
            "ticket",
        ]


class ListLikesSerializer(BaseLikesSerializer):
    class Meta(BaseLikesSerializer.Meta): ...

class RetrieveLikesSerializer(BaseLikesSerializer):
    class Meta(BaseLikesSerializer.Meta): ...


class CreateLikesSerializer(BaseLikesSerializer):
    ticket = serializers.PrimaryKeyRelatedField(queryset=TicketsModel.objects.all())

    class Meta(BaseLikesSerializer.Meta):
        fields = [
            "id",
            "ticket",
        ]

    def create(self, validated_data):
        user = self.context["request"].user  # type: ignore
        ticket = validated_data["ticket"]

        if LikesModel.objects.filter(user=user, ticket=ticket).exists():
            raise serializers.ValidationError("You have already made this ticket..")

        validated_data["user_id"] = user.id
        return LikesModel.objects.create(**validated_data)
