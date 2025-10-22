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
    role = serializers.CharField(write_only=True, required=True)

    class Meta(BaseEmployeesSerializer.Meta):
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "password",
            "role"
        ]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        role_status = validated_data.pop("role", None)
        if not role_status:
            raise serializers.ValidationError("Role status is required")

        password = validated_data.pop("password", None)
        user = get_user_model().objects.create(**validated_data)
        user.role = role_status

        if password:
            user.set_password(password)
            user.save()

        return user
