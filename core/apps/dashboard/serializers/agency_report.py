from rest_framework import serializers
from core.apps.accounts.models import TravelAgency, TravelAgencyDocuments, ParticipantModel
from core.apps.tickets.models import TicketsModel, TicketorderModel, TicketsCommentsModel
from core.apps.tickets.choices import OrderStatusChoices
from django.contrib.auth import get_user_model
from django.db.models import Q, Avg


class UserModelSerializer(serializers.ModelSerializer):
    contact = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "contact"
        ]

    def get_contact(self, obj):
        phone_number = obj.phone
        if phone_number:
            return phone_number
        return obj.email


class OrderSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)

    class Meta:
        model = TicketorderModel
        fields = [
            "id",
            "user",
            "total_price",
            "departure_date",
            "arrival_time",
            "created_at",
        ]


class CommentSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)

    class Meta:
        model = TicketsCommentsModel
        fields = [
            "user",
            "text",
            "rating",
            "ticket",
            "created",
        ]


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
    class Meta(BaseDashboardTravelAgencyReportSerializer.Meta):
        fields = [
            "id",
            "name",
            "custom_id",
            "paid",
            "pending",
            "ticket_sold_count",
            "ticket_count",
        ]


class RetrieveDashboardTravelAgencyReportSerializer(BaseDashboardTravelAgencyReportSerializer):
    total_booking_count = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()
    orders = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta(BaseDashboardTravelAgencyReportSerializer.Meta):
        fields = [
            "id",
            "name",
            "custom_id",
            "share_percentage",
            "addres",
            "email",
            "phone",
            "web_site",
            "paid",
            "pending",
            "ticket_sold_count",
            "ticket_count",
            "total_income",
            "platform_income",
            "total_booking_count",
            "rating",
            "orders",  # 🆕 qo‘shildi
            "comments",  # 🆕 qo‘shildi
        ]

    def get_total_booking_count(self, obj):
        return TicketorderModel.objects.filter(
            ticket__travel_agency=obj
        ).filter(
            Q(order_status=OrderStatusChoices.COMPLETED) |
            Q(order_status=OrderStatusChoices.CONFIRMED)
        ).count()

    def get_rating(self, obj):
        return TicketsCommentsModel.objects.filter(
            ticket__travel_agency=obj
        ).aggregate(
            avg_score=Avg('rating')
        )['avg_score'] or 0

    def get_orders(self, obj):
        """Agentlikka tegishli barcha orderlar"""
        orders = TicketorderModel.objects.filter(ticket__travel_agency=obj)
        return OrderSerializer(orders, many=True).data

    def get_comments(self, obj):
        """Agentlikka tegishli barcha kommentlar"""
        comments = TicketsCommentsModel.objects.filter(ticket__travel_agency=obj)
        return CommentSerializer(comments, many=True).data
