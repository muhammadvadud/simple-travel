from rest_framework import serializers
from core.apps.accounts.models import TravelAgency, TravelAgencyDocuments
from core.apps.tickets.models import TicketsModel


class TravelAgencyDocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelAgencyDocuments
        fields = [
            "file",
        ]


class BaseDashboardTravelAgencyReportSerializer(serializers.ModelSerializer):
    travel_agency_documents = TravelAgencyDocumentsSerializer(many=True, read_only=True)
    ticket_count = serializers.SerializerMethodField()

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
            "total_income",
            "paid",
            "pending",
        ]

    def get_ticket_count(self, obj):
        count = TicketsModel.objects.filter(travel_agency=obj).count()
        return count


class ListDashboardTravelAgencyReportSerializer(BaseDashboardTravelAgencyReportSerializer):
    ticket_count = serializers.SerializerMethodField()

    class Meta(BaseDashboardTravelAgencyReportSerializer.Meta):
        fields = [
            "id",
            "name",
            "paid",
            "pending",
            "ticket_sold_count",
            "ticket_count",
        ]

    def get_ticket_count(self, obj):
        count = TicketsModel.objects.filter(travel_agency=obj).count()
        return count


class RetrieveDashboardTravelAgencyReportSerializer(BaseDashboardTravelAgencyReportSerializer):
    class Meta(BaseDashboardTravelAgencyReportSerializer.Meta): ...
