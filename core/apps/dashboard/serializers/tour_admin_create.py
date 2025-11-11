from core.apps.accounts.choices import RoleChoice
from core.apps.accounts.models import TravelAgency
from django.utils import timezone
#   +888 88 888 88 88

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError
from core.apps.accounts.models.travel_agency import TravelAgency
import random


class TravelAgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = TravelAgency
        fields = [
            "name",
            "phone",
            "email",
            "custom_id",
        ]


class BaseTourAdminSerializer(serializers.ModelSerializer):
    travel_agency = TravelAgencySerializer()

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "first_name",
            "last_name",
            "phone",
            "role",
            "travel_agency",
        ]


class ListTourAdminSerializer(BaseTourAdminSerializer):
    class Meta(BaseTourAdminSerializer.Meta): ...


class RetrieveTourAdminSerializer(BaseTourAdminSerializer):
    class Meta(BaseTourAdminSerializer.Meta): ...


class CreateTourAdminSerializer(serializers.Serializer):

    def create(self, validated_data):
        request = self.context.get("request")
        pk = request.parser_context["kwargs"].get("pk")
        try:
            travel_agency = TravelAgency.objects.get(pk=pk)
            phone_number = travel_agency.phone
        except TravelAgency.DoesNotExist:
            raise ValidationError("Travel Agency does not exist")
        user_check = get_user_model().objects.filter(phone=phone_number)
        if user_check.exists():
            user_check.delete()

        user = get_user_model().objects.create(
            phone=phone_number,
            role=RoleChoice.TourAdmin,
            travel_agency=travel_agency,
            validated_at=timezone.now(),

        )
        password = str(random.randint(100000, 999999))
        user.set_password(password)
        user.save()
        user.generated_password = password

        return user

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "phone": instance.phone,
            "role": instance.role,
            "travel_agency": instance.travel_agency.name if instance.travel_agency else None,
            "password": getattr(instance, "generated_password", None),
        }


class UpdateTourAdminPasswordSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        password = str(random.randint(100000, 999999))
        instance.set_password(password)
        instance.save()
        instance.generated_password = password
        return instance

    def to_representation(self, instance):
        return {
            "id": instance.id,
            "phone": instance.phone,
            "role": instance.role,
            "travel_agency": instance.travel_agency.name if instance.travel_agency else None,
            "password": getattr(instance, "generated_password", None),
        }
