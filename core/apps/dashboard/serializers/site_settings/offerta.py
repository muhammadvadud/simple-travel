from rest_framework import serializers
from core.apps.dashboard.models import Offerta


class BaseOffertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offerta
        fields = [
            "id",
            "title",
            "title_uz",
            "title_ru",
            "content",
            "content_uz",
            "content_ru",
            "person_type",
            "is_active",
        ]


class ListOffertaSerializer(BaseOffertaSerializer):
    class Meta(BaseOffertaSerializer.Meta): ...


class RetrieveOffertaSerializer(BaseOffertaSerializer):
    class Meta(BaseOffertaSerializer.Meta): ...


class CreateOffertaSerializer(BaseOffertaSerializer):
    class Meta(BaseOffertaSerializer.Meta): ...


class PublicOffertaSerializer(BaseOffertaSerializer):
    class Meta(BaseOffertaSerializer.Meta):
        fields = [
            "id",
            "title",
            "content",
            "person_type",
            "is_active",
        ]
