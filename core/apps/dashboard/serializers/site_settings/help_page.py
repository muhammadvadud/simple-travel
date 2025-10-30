from rest_framework import serializers
from core.apps.dashboard.models import HelpPage


class BaseHelpPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpPage
        fields = [
            "id",
            "title",
            "title_uz",
            "title_ru",
            "content",
            "content_uz",
            "content_ru",
            "page_type",
            "is_active",
        ]


class ListHelpPageSerializer(BaseHelpPageSerializer):
    class Meta(BaseHelpPageSerializer.Meta): ...


class RetrieveHelpPageSerializer(BaseHelpPageSerializer):
    class Meta(BaseHelpPageSerializer.Meta): ...


class CreateHelpPageSerializer(BaseHelpPageSerializer):
    class Meta(BaseHelpPageSerializer.Meta): ...


class PublicHelpPageSerializer(BaseHelpPageSerializer):
    class Meta(BaseHelpPageSerializer.Meta):
        fields = [
            "id",
            "title",
            "content",
            "page_type",
            "is_active",
        ]
