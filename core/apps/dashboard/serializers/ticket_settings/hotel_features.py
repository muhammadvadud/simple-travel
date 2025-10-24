from rest_framework import serializers
from core.apps.tickets.models import HotelFeatureModel, HotelFeatureTypeModel


class HotelFeatureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFeatureTypeModel
        fields = [
            "id",
            "hotel_feature_type_name",
            "hotel_feature_type_name_ru"
        ]


class BaseHotelFeatureSerializer(serializers.ModelSerializer):
    feature_type = HotelFeatureTypeSerializer(read_only=True)

    class Meta:
        model = HotelFeatureModel
        fields = [
            "id",
            "feature_name",
            "feature_name_ru",
            "feature_type",
        ]


class ListHotelFeatureSerializer(BaseHotelFeatureSerializer):
    class Meta(BaseHotelFeatureSerializer.Meta): ...


class RetrieveHotelFeatureSerializer(BaseHotelFeatureSerializer):
    class Meta(BaseHotelFeatureSerializer.Meta): ...


class CreateHotelFeatureSerializer(BaseHotelFeatureSerializer):
    feature_type = serializers.PrimaryKeyRelatedField(queryset=HotelFeatureTypeModel.objects.all(), write_only=True)

    class Meta(BaseHotelFeatureSerializer.Meta):
        fields = [
            "id",
            "feature_name",
            "feature_name_ru",
            "feature_type",
        ]
