from rest_framework import serializers
from django.contrib.auth import get_user_model


class BaseEmployeesSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "email",
            "role",
        ]


class ListEmployeesSerializer(BaseEmployeesSerializer):
    class Meta(BaseEmployeesSerializer.Meta): ...


class RetrieveEmployeesSerializer(BaseEmployeesSerializer):
    class Meta(BaseEmployeesSerializer.Meta): ...


class CreateEmployeesSerializer(BaseEmployeesSerializer):
    role_status = serializers.CharField(write_only=True, required=True)

    class Meta(BaseEmployeesSerializer.Meta):
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "role_status"
        ]

    def create(self, validated_data):
        role_status = validated_data.pop("role_status", [])
        if not role_status:
            raise serializers.ValidationError("Role status is required")
        validated_data["role"] = role_status
        user = get_user_model().objects.create(**validated_data)
        return user
