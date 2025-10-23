from rest_framework import serializers
from core.apps.tickets.models.hotel import (
    HotelModel,
    HotelAmenitiesModel,
    HotelTypeModel,
    HotelFeatureModel,
)


class BaseHotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HotelModel
        fields = ["id"]


class ListHotelSerializer(BaseHotelSerializer):
    class Meta(BaseHotelSerializer.Meta):
        fields = [
            "id",
            "name",
            "rating",
            "meal_plan",
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
        queryset=HotelAmenitiesModel.objects.all(),
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
        amenities = validated_data.pop("hotel_amenities", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if amenities is not None:
            instance.hotel_amenities.set(amenities)

        return instance
