from rest_framework import serializers

from core.apps.accounts.models import TravelAgency, TravelAgencyDocuments


class BaseTravelAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelAgency
        fields = [
            "id",
            "status",
            "share_percentage",
            "name",
            "addres",
            "email",
            "phone",
            "web_site",
        ]


class ListTravelAgencySerializer(BaseTravelAgencySerializer):
    class Meta(BaseTravelAgencySerializer.Meta): ...


class RetrieveTravelAgencySerializer(BaseTravelAgencySerializer):
    class Meta(BaseTravelAgencySerializer.Meta): ...


class CreateTravelAgencySerializer(BaseTravelAgencySerializer):
    documents = serializers.ListField(child=serializers.FileField(), write_only=True, required=True)
    web_site = serializers.CharField(write_only=True, required=False)

    class Meta(BaseTravelAgencySerializer.Meta):
        fields = [
            "name",
            "addres",
            "email",
            "phone",
            "web_site",
            "documents",
        ]

    def create(self, validated_data):
        documents = validated_data.pop("documents", [])
        travel_agency = TravelAgency.objects.create(**validated_data)
        if documents:
            for doc in documents:
                TravelAgencyDocuments.objects.create(travel_agency=travel_agency, file=doc)
        return travel_agency
