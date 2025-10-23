from rest_framework import serializers
from core.apps.accounts.models import SupportModel


class BaseSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportModel
        fields = [
            "id",
            "name",
            "phone_number",
            "travel_agency",
        ]


class ListSupportSerializer(BaseSupportSerializer):
    class Meta(BaseSupportSerializer.Meta): ...


class RetrieveSupportSerializer(BaseSupportSerializer):
    class Meta(BaseSupportSerializer.Meta): ...
