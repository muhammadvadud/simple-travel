from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from .tickets import TicketsModel, TicketsAmenitiesModel


class HotelMealPlan(AbstractBaseModel):
    name = models.CharField(max_length=255, verbose_name=_('name'))

    def __str__(self):
        return str(self.pk)

    class Meta:
        db_table = 'hotel_meal_plan'
        verbose_name = _('hotel meal plan')
        verbose_name_plural = _('hotel meal plans')


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


# >>>>>>>>>>>>>>Hozircha ishlatilmaydi
# class HotelAmenitiesModel(AbstractBaseModel):
#     name = models.CharField(max_length=255, verbose_name=_("name"))
#     icon_name = models.CharField(max_length=255, verbose_name=_("icon name"))
#
#     def __str__(self):
#         return self.name
#
#     @classmethod
#     def _create_fake(self):
#         return self.objects.create(
#             name="mock",
#             icon_name="mock",
#         )
#
#     class Meta:
#         db_table = "hotel_amenities"
#         verbose_name = _("Hotel Amenity")
#         verbose_name_plural = _("Hotel Amenities")


# >>>>>>>>>>>>>>

class HotelFeatureTypeModel(AbstractBaseModel):
    hotel_feature_type_name = models.CharField(verbose_name=_("hotel feature type name"), max_length=255)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            hotel_feature_type_name="mock",

        )

    class Meta:
        db_table = "hotel_feature_type"
        verbose_name = _("HotelFeatureTypeModel")
        verbose_name_plural = _("HotelFeatureTypeModels")


class HotelFeatureModel(AbstractBaseModel):
    feature_type = models.ForeignKey(HotelFeatureTypeModel, on_delete=models.CASCADE)
    feature_name = models.CharField(verbose_name=_("hotel feature name"), max_length=255)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            feature_type=HotelFeatureTypeModel._create_fake(),
            feature_name="mock",

        )

    class Meta:
        db_table = "hotel_feature"
        verbose_name = _("HotelFeatureModel")
        verbose_name_plural = _("HotelFeatureModels")


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
    meal_plan = models.ForeignKey(HotelMealPlan, related_name="meal_plan", verbose_name=_("meal plan"),
                                  on_delete=models.SET_NULL, null=True, blank=True)
    hotel_type = models.ManyToManyField(HotelTypeModel, verbose_name=_("hotel type"))
    hotel_amenities = models.ManyToManyField(TicketsAmenitiesModel, blank=True, verbose_name=_("hotel amenities"))
    hotel_features = models.ManyToManyField(HotelFeatureModel, verbose_name=_("hotel features"), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            ticket=TicketsModel._create_fake(),
            name="mock",
            rating=4.5,
        )

    class Meta:
        db_table = "hotel"
        verbose_name = _("HotelModel")
        verbose_name_plural = _("HotelModels")
