from rest_framework import serializers, status
from rest_framework.response import Response

from core.apps.accounts.models import LikesModel


class BaseLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikesModel
        fields = [
            "ticket"
        ]

        def delete(self):
            user = self.context["request"].user  # type: ignore
            like_id = self.context["view"].kwargs.get("pk")  # type: ignore
            like = LikesModel.objects.get(pk=like_id)
            if like:
                if like.user == user:
                    like.delete()
                raise serializers.ValidationError("Like is not yours")
            raise serializers.ValidationError("Like not found")


class ListLikesSerializer(BaseLikesSerializer):
    class Meta(BaseLikesSerializer.Meta): ...


class RetrieveLikesSerializer(BaseLikesSerializer):
    class Meta(BaseLikesSerializer.Meta): ...


class CreateLikesSerializer(BaseLikesSerializer):
    class Meta(BaseLikesSerializer.Meta):
        fields = [
            "ticket",
        ]

    def create(self, validated_data):
        user = self.context["request"].user  # type: ignore
        ticket = validated_data["ticket"]

        if LikesModel.objects.filter(user=user, ticket=ticket).exists():
            raise serializers.ValidationError("You have already made this ticket..")

        validated_data["user_id"] = user.id
        return LikesModel.objects.create(**validated_data)
