from rest_framework import serializers
from core.apps.api.models import FaqCategoryModel


class BaseFaqCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqCategoryModel
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
        ]


class ListFaqCategorySerializer(BaseFaqCategorySerializer):
    class Meta(BaseFaqCategorySerializer.Meta): ...


class RetrieveFaqCategorySerializer(BaseFaqCategorySerializer):
    class Meta(BaseFaqCategorySerializer.Meta): ...


class CreateFaqCategorySerializer(BaseFaqCategorySerializer):
    class Meta(BaseFaqCategorySerializer.Meta):
        fields = [
            "id",
            "name",
            "name_ru",
        ]
