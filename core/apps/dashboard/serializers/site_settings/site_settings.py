from rest_framework import serializers
from core.apps.dashboard.models import SiteSettings
from django.core.exceptions import ValidationError


class BaseSiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = [
            "id",
            "address",
            "latitude",
            "longitude",
            "telegram",
            "instagram",
            "facebook",
            "twitter",
            "email",
            "main_phone",
            "other_phone",
        ]


class ListSiteSettingsSerializer(BaseSiteSettingsSerializer):
    class Meta(BaseSiteSettingsSerializer.Meta): ...


class RetrieveSiteSettingsSerializer(BaseSiteSettingsSerializer):
    class Meta(BaseSiteSettingsSerializer.Meta): ...


class CreateSiteSettingsSerializer(BaseSiteSettingsSerializer):
    class Meta(BaseSiteSettingsSerializer.Meta): ...

    def validate(self, attrs):
        if not self.instance and SiteSettings.objects.exists():
            raise ValidationError("Faqat bitta SiteSettings yozuvi bo‘lishi mumkin.")
        return attrs
