from rest_framework import serializers
from core.apps.tickets.models import (
    HotelModel,
    TicketsAmenitiesModel,
    HotelTypeModel,
    HotelFeatureModel,
    HotelFeatureTypeModel,
    HotelMealPlan

)


class HotelMealPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelMealPlan
        fields = [
            "name_ru",
            "name_uz"
        ]


class HotelFeatureTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelFeatureTypeModel
        fields = [
            "id",
            "hotel_feature_type_name_ru",
            "hotel_feature_type_name_uz",
        ]


class HotelFeatureSerializer(serializers.ModelSerializer):
    feature_type = HotelFeatureTypeSerializer(read_only=True)

    class Meta:
        model = HotelFeatureModel
        fields = ["id", "feature_name", "feature_name_uz", "feature_name_ru", "feature_type"]


class HotelTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelTypeModel
        fields = ["id", "name", "name_ru", "name_uz"]


class HotelAmenitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketsAmenitiesModel
        fields = [
            "name",
            "name_ru",
            "name_uz",
            "icon_name"
        ]


class BaseHotelSerializer(serializers.ModelSerializer):
    meal_plan = HotelMealPlanSerializer(read_only=True)

    class Meta:
        model = HotelModel
        fields = ["id"]


class ListHotelSerializer(BaseHotelSerializer):
    hotel_amenities = HotelAmenitiesSerializer(many=True, read_only=True)
    hotel_type = HotelTypeSerializer(many=True, read_only=True)
    hotel_features = HotelFeatureSerializer(many=True, read_only=True)

    class Meta(BaseHotelSerializer.Meta):
        fields = [
            "id",
            "name",
            "rating",
            "meal_plan",
            "ticket",
            "hotel_type",
            "hotel_amenities",
            "hotel_features",
        ]


class RetrieveHotelSerializer(BaseHotelSerializer):
    class Meta(BaseHotelSerializer.Meta):
        fields = [
            "id",
            "name",
            "rating",
            "meal_plan",
            "hotel_type",
            "hotel_amenities",
            "hotel_features",
            "created_at",
            "updated_at",
        ]


class CreateHotelSerializer(serializers.ModelSerializer):
    hotel_amenities = serializers.PrimaryKeyRelatedField(
        queryset=TicketsAmenitiesModel.objects.all(),
        many=True,
        required=False
    )
    hotel_type = serializers.PrimaryKeyRelatedField(
        queryset=HotelTypeModel.objects.all(),
        many=True,
        required=False
    )
    hotel_features = serializers.PrimaryKeyRelatedField(
        queryset=HotelFeatureModel.objects.all(),
        many=True,
        required=False
    )
    meal_plan = serializers.PrimaryKeyRelatedField(queryset=HotelMealPlan.objects.all())

    class Meta:
        model = HotelModel
        fields = [
            "id",
            "ticket",
            "name",
            "rating",
            "meal_plan",
            "hotel_type",
            "hotel_amenities",
            "hotel_features",
        ]

    def create(self, validated_data):
        amenities = validated_data.pop("hotel_amenities", [])
        hotel_type = validated_data.pop("hotel_type", [])
        features = validated_data.pop("hotel_features", [])

        hotel = HotelModel.objects.create(**validated_data)

        if amenities:
            hotel.hotel_amenities.set(amenities)

        if hotel_type:
            hotel.hotel_type.set(hotel_type)
        if features:
            hotel.hotel_features.set(features)

        return hotel

    def update(self, instance, validated_data):
        amenities = validated_data.pop("hotel_amenities", [])
        hotel_type = validated_data.pop("hotel_type", [])
        features = validated_data.pop("hotel_features", [])

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if amenities:
            instance.hotel_amenities.set(amenities)

        if hotel_type:
            instance.hotel_type.set(hotel_type)

        if features:
            instance.hotel_features.set(features)

        return instance
