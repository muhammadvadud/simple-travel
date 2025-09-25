from config.env import env
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from rest_framework import exceptions, serializers

OTP_SIZE = env.int("OTP_SIZE", 4)


class EmailRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()

    def validate_phone(self, value):
        user = get_user_model().objects.filter(email=value, validated_at__isnull=False)
        if user.exists():
            raise exceptions.ValidationError(_("Email already registered."), code="unique")
        return value

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "email", "password"]
        extra_kwargs = {
            "first_name": {
                "required": True,
            },
            "last_name": {"required": True},
        }


class EmailConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=OTP_SIZE, min_length=OTP_SIZE)
    email = serializers.EmailField()


class EmailResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate_email(self, value):
        user = get_user_model().objects.filter(email=value)
        if user.exists():
            return value

        raise serializers.ValidationError(_("User does not exist"))


class EmailResetConfirmationSerializer(serializers.Serializer):
    code = serializers.CharField(min_length=OTP_SIZE, max_length=OTP_SIZE)
    email = serializers.EmailField()

    def validate_email(self, value):
        user = get_user_model().objects.filter(email=value)
        if user.exists():
            return value
        raise serializers.ValidationError(_("User does not exist"))


class EmailResendSerializer(serializers.Serializer):
    email = serializers.EmailField()
