from rest_framework import serializers
from core.apps.api.models import FaqModel, FaqCategoryModel


class FaqCategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqCategoryModel
        fields = [
            "name",
        ]


class BaseFaqSerializer(serializers.ModelSerializer):
    category = FaqCategoryModelSerializer(read_only=True)

    class Meta:
        model = FaqModel
        fields = [
            "id",
            "title",
            "title_ru",
            "title_uz",
            "text",
            "text_ru",
            "text_uz",
            "category",
        ]


class ListFaqSerializer(BaseFaqSerializer):
    class Meta(BaseFaqSerializer.Meta): ...


class RetrieveFaqSerializer(BaseFaqSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=FaqCategoryModel.objects.all(),
        write_only=True,
        required=True
    )

    class Meta(BaseFaqSerializer.Meta):
        fields = [
            "id",
            "title",
            "title_ru",
            "title_uz",
            "text",
            "text_ru",
            "text_uz",
            "category",
        ]


class CreateFaqSerializer(BaseFaqSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset=FaqCategoryModel.objects.all(),
        write_only=True,
        required=True
    )

    class Meta(BaseFaqSerializer.Meta):
        fields = [
            "id",
            "title",
            "title_ru",
            "text",
            "text_ru",
            "category",
        ]
