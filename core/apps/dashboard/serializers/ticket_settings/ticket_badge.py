from rest_framework import serializers
from core.apps.tickets.models import BadgeModel


class BaseBadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BadgeModel
        fields = [
            "id",
            "name",
            "color",
        ]


class ListBadgeSerializer(BaseBadgeSerializer):
    class Meta(BaseBadgeSerializer.Meta): ...


class RetrieveBadgeSerializer(BaseBadgeSerializer):
    class Meta(BaseBadgeSerializer.Meta): ...


class CreateBadgeSerializer(BaseBadgeSerializer):
    class Meta(BaseBadgeSerializer.Meta):
        fields = [
            "id",
            "name",
            "color",
        ]
