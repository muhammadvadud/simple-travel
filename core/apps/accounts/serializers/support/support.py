from rest_framework import serializers

from core.apps.accounts.models import SupportModel


class BaseSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportModel
        fields = [
            "id",
            "name",
        ]


class ListSupportSerializer(BaseSupportSerializer):
    class Meta(BaseSupportSerializer.Meta): ...


class RetrieveSupportSerializer(BaseSupportSerializer):
    class Meta(BaseSupportSerializer.Meta): ...


class CreateSupportSerializer(BaseSupportSerializer):
    class Meta(BaseSupportSerializer.Meta):
        fields = [
            "name",
            "phone_number",
        ]
