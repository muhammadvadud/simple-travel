from rest_framework import serializers
from core.apps.accounts.models import TravelAgency
from core.apps.tickets.models import TicketsModel
from django.db.models import Sum


class BaseTravelAgencySerializer(serializers.ModelSerializer):
    owner_user = serializers.SerializerMethodField()
    tour_count = serializers.SerializerMethodField()

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
            'tour_count',
            'ticket_sold_count',
            'total_income'
        ]

    def get_owner_user(self, obj):
        user = obj.admins.first()
        if not user:
            return None
        return f"{user.first_name} {user.last_name}"

    def get_tour_count(self, obj):
        tour_count = obj.tickets.count()
        if not tour_count:
            return None
        return tour_count


class ListTravelAgencySerializer(BaseTravelAgencySerializer):
    class Meta(BaseTravelAgencySerializer.Meta):
        fields = [
            'status',
            'custom_id',
            'name',
            'owner_user',
            'share_percentage',
            'tour_count',
            'ticket_sold_count',
            'total_income',
        ]


class FullListTravelAgencySerializer(serializers.Serializer):
    list = ListTravelAgencySerializer(many=True, read_only=True)
    all_tour_agency = serializers.SerializerMethodField()
    activate_tour_agency = serializers.SerializerMethodField()
    all_tickets = serializers.SerializerMethodField()
    total_income = serializers.SerializerMethodField()

    def get_all_tour_agency(self, obj):
        tour_agency = TravelAgency.objects.all().count()
        if not tour_agency:
            return None
        return tour_agency

    def get_activate_tour_agency(self, obj):
        tour_agency = TravelAgency.objects.filter(status='approved').count()
        if not tour_agency:
            return None
        return tour_agency

    def get_all_tickets(self, obj):
        tickets = TicketsModel.objects.all().count()
        if not tickets:
            return None
        return tickets

    def get_total_income(self, obj):
        total = TravelAgency.objects.aggregate(total=Sum("total_income"))["total"]
        return total or 0


class RetrieveTravelAgencySerializer(BaseTravelAgencySerializer):
    class Meta(BaseTravelAgencySerializer.Meta): ...


class CreateTravelAgencySerializer(BaseTravelAgencySerializer):
    class Meta(BaseTravelAgencySerializer.Meta): ...
