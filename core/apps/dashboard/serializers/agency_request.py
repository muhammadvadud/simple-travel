from rest_framework import serializers
from core.apps.accounts.models import TravelAgency, TravelAgencyDocuments


class TravelAgencyDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelAgencyDocuments
        fields = [
            "file",
        ]


class BaseDashboardTravelAgencyRequestSerializer(serializers.ModelSerializer):
    travel_agency_documents = TravelAgencyDocumentsSerializer(many=True, read_only=True)

    class Meta:
        model = TravelAgency
        fields = [
            "id",
            "status",
            "name",
            "addres",
            "email",
            "phone",
            "web_site",
        ]


class ListDashboardTravelAgencyRequestSerializer(BaseDashboardTravelAgencyRequestSerializer):
    class Meta(BaseDashboardTravelAgencyRequestSerializer.Meta):
        fields = [
            "id",
            "status",
            "name",
            "addres",
            "email",
            "phone",
            "web_site",
            "travel_agency_documents",
        ]


class RetrieveDashboardTravelAgencyRequestSerializer(BaseDashboardTravelAgencyRequestSerializer):
    class Meta(BaseDashboardTravelAgencyRequestSerializer.Meta):
        fields = [
            "status",
            "share_percentage"
        ]
