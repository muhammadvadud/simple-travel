from modeltranslation.translator import TranslationOptions, register

from core.apps.tickets.models import HotelModel, HotelTypeModel, HotelFeatureTypeModel, \
    HotelFeatureModel, HotelMealPlan


@register(HotelMealPlan)
class HotelMealPlanTranslation(TranslationOptions):
    fields = [
        "name"
    ]


@register(HotelModel)
class HotelTranslation(TranslationOptions):
    fields = [
    ]


@register(HotelTypeModel)
class HotelTypeModelTranslation(TranslationOptions):
    fields = [
        "name",
    ]


@register(HotelFeatureTypeModel)
class HotelFeatureTypeModelTranslation(TranslationOptions):
    fields = [
        "hotel_feature_type_name",
    ]


@register(HotelFeatureModel)
class HotelFeatureModelTranslation(TranslationOptions):
    fields = [
        "feature_name",
    ]
