from rest_framework import serializers
from core.apps.accounts.models import TravelAgency
from django.contrib.auth import get_user_model


class BaseTravelAgencySerializer(serializers.ModelSerializer):
    owner_user = serializers.SerializerMethodField()

    class Meta:
        model = TravelAgency
        fields = [
            'status',
            'custom_id',
            'share_percentage',
            'name',
            'addres',
            'email',
            'phone',
            'web_site',
            'owner_user',
        ]

    def get_owner_user(self, obj):
        user = obj.admins.first()
        if not user:
            return None
        return f"{user.first_name} {user.last_name}"


class ListTravelAgencySerializer(BaseTravelAgencySerializer):
    class Meta(BaseTravelAgencySerializer.Meta):
        fields = [
            'status',
            'custom_id',
            'share_percentage',
            'name',
            'owner_user',
        ]


class RetrieveTravelAgencySerializer(BaseTravelAgencySerializer):
    class Meta(BaseTravelAgencySerializer.Meta): ...


class CreateTravelAgencySerializer(BaseTravelAgencySerializer):
    class Meta(BaseTravelAgencySerializer.Meta): ...
