from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model


class PhoneTokenObtainPairSerializer(serializers.Serializer):
    phone = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        phone = attrs.get("phone")
        password = attrs.get("password")

        try:
            user = get_user_model().objects.get(phone=phone)
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError(_("Bunday telefon raqam mavjud emas."))

        if not user.check_password(password):
            raise serializers.ValidationError(_("Parol noto‘g‘ri."))

        if not user.is_active:
            raise serializers.ValidationError(_("Foydalanuvchi faol emas."))

        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
