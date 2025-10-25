from rest_framework import serializers
from core.apps.dashboard.models import SiteSeo
from django.core.exceptions import ValidationError


class BaseSiteSeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSeo
        fields = [
            "id",
            "title",
            "description",
            "keywords",
            "og_title",
            "og_description",
            "og_image",
        ]


class ListSiteSeoSerializer(BaseSiteSeoSerializer):
    class Meta(BaseSiteSeoSerializer.Meta): ...


class RetrieveSiteSeoSerializer(BaseSiteSeoSerializer):
    class Meta(BaseSiteSeoSerializer.Meta): ...


class CreateSiteSeoSerializer(BaseSiteSeoSerializer):
    class Meta(BaseSiteSeoSerializer.Meta): ...

    def validate(self, attrs):
        if not self.instance and SiteSeo.objects.exists():
            raise ValidationError("Faqat bitta SiteSeo yozuvi bo‘lishi mumkin.")
        return attrs
