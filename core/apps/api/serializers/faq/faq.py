from rest_framework import serializers

from core.apps.api.models import FaqModel, FaqCategoryModel


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqModel
        fields = ["id", "title", "text"]


class FaqCategoryWithFaqsSerializer(serializers.ModelSerializer):
    faqs = FaqSerializer(many=True, read_only=True)

    class Meta:
        model = FaqCategoryModel
        fields = ["id", "name", "faqs"]


class BaseFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqModel
        fields = [
            "id",
            "title",
            "text",
            "category",
        ]


class ListFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...


class RetrieveFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...


class CreateFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta):
        fields = [
            "id",
            "name",
        ]
