from rest_framework import serializers
from core.apps.dashboard.models import HelpPage


class BaseHelpPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HelpPage
        fields = [
            "id",
            "title",
            "content",
            "page_type",
            "is_active",
        ]


class ListHelpPageSerializer(BaseHelpPageSerializer):
    class Meta(BaseHelpPageSerializer.Meta): ...


class RetrieveHelpPageSerializer(BaseHelpPageSerializer):
    class Meta(BaseHelpPageSerializer.Meta): ...


class CreateHelpPageSerializer(BaseHelpPageSerializer):
    class Meta(BaseHelpPageSerializer.Meta): ...
