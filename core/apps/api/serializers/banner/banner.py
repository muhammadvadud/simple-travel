from rest_framework import serializers

from core.apps.api.models import BannerModel


class BaseBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = [
            "id",
            "name",
        ]


class ListBannerSerializer(BaseBannerSerializer):
    class Meta(BaseBannerSerializer.Meta): ...


class RetrieveBannerSerializer(BaseBannerSerializer):
    class Meta(BaseBannerSerializer.Meta): ...


class CreateBannerSerializer(BaseBannerSerializer):
    class Meta(BaseBannerSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
