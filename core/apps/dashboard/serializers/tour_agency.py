from rest_framework import serializers
from core.apps.accounts.models import TravelAgency


class BaseTravelAgencySerializer(serializers.ModelSerializer):
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
        ]


class ListTravelAgencySerializer(BaseTravelAgencySerializer):
    class Meta(BaseTravelAgencySerializer.Meta): ...


class RetrieveTravelAgencySerializer(BaseTravelAgencySerializer):
    class Meta(BaseTravelAgencySerializer.Meta): ...


class CreateTravelAgencySerializer(BaseTravelAgencySerializer):
    class Meta(BaseTravelAgencySerializer.Meta):...
