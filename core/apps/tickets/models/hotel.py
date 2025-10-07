from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.tickets.choises.hotel_feature import HotelFeature
from .tickets import TicketsModel


class HotelTypeModel(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "hotel_types"
        verbose_name = _("HotelTypeModel")
        verbose_name_plural = _("HotelTypeModels")


class HotelAmenitiesModel(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_("name"))

    def __str__(self):
        return self.name

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "hotel_amenities"
        verbose_name = _("Hotel Amenity")
        verbose_name_plural = _("Hotel Amenities")


class HotelModel(AbstractBaseModel):
    MEAL_PLAN_CHOICES = [
        ("all_inclusive", "All Inclusive"),
        ("breakfast", "Breakfast Only"),
        ("half_board", "Half Board"),
        ("full_board", "Full Board"),
    ]

    ticket = models.ForeignKey(TicketsModel, related_name="ticket_hotel", verbose_name=_("ticket"),
                               on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_("name"), max_length=255)
    rating = models.FloatField(verbose_name=_("rating"), blank=True, null=True)
    meal_plan = models.CharField(verbose_name=_("meal plan"), choices=MEAL_PLAN_CHOICES, max_length=255,
                                 default="breakfast")
    hotel_type = models.ManyToManyField(HotelTypeModel, verbose_name=_("hotel type"))
    hotel_amenities = models.ManyToManyField(HotelAmenitiesModel, verbose_name=_("hotel amenities"))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            ticket=TicketsModel._create_fake(),
            name="mock",
            website="https://www.default.com/",
            rating=4.5,
        )

    class Meta:
        db_table = "hotel"
        verbose_name = _("HotelModel")
        verbose_name_plural = _("HotelModels")


class HotelFeatureModel(AbstractBaseModel):
    hotel = models.ForeignKey(HotelModel, verbose_name=_("hotel"), on_delete=models.CASCADE)
    hotel_feature_choice = models.CharField(verbose_name=_("hotel feature choice"), choices=HotelFeature,
                                            max_length=255)
    hotel_feature_name = models.CharField(verbose_name=_("hotel feature name"), max_length=255)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            hotel=HotelModel._create_fake(),
            hotel_feature_name="mock",
            hotel_feature_choice="children_section",

        )

    class Meta:
        db_table = "hotel_feature"
        verbose_name = _("HotelFeatureModel")
        verbose_name_plural = _("HotelFeatureModels")
