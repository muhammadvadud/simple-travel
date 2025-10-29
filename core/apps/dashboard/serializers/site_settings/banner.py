from rest_framework import serializers
from core.apps.api.models import BannerModel


class BaseBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerModel
        fields = [
            "id",
            "title",
            "title_ru",
            "description",
            "description_ru",
            "image",
            "link",
            "position",
        ]


class ListBannerSerializer(BaseBannerSerializer):
    class Meta(BaseBannerSerializer.Meta):
        fields = [
            "id",
            "title",
            "title_ru",
            "title_uz",
            "description",
            "description_ru",
            "description_uz",
            "image",
            "link",
            "position",
        ]


class RetrieveBannerSerializer(BaseBannerSerializer):
    class Meta(BaseBannerSerializer.Meta): ...


class CreateBannerSerializer(BaseBannerSerializer):
    class Meta(BaseBannerSerializer.Meta): ...
