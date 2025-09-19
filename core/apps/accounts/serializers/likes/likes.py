from rest_framework import serializers

from core.apps.accounts.models import LikesModel


class BaseLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikesModel
        fields = [
            "id",
            "user",
        ]


class ListLikesSerializer(BaseLikesSerializer):
    class Meta(BaseLikesSerializer.Meta): ...


class RetrieveLikesSerializer(BaseLikesSerializer):
    class Meta(BaseLikesSerializer.Meta): ...


class CreateLikesSerializer(BaseLikesSerializer):
    class Meta(BaseLikesSerializer.Meta):
        fields = [
            "id",
            "user",
        ]
