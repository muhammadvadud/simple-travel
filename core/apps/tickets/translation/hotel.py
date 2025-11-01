from modeltranslation.translator import TranslationOptions, register

from core.apps.tickets.models import HotelModel, HotelTypeModel,  HotelFeatureTypeModel, \
    HotelFeatureModel


@register(HotelModel)
class HotelTranslation(TranslationOptions):
    fields = [
        "name",
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
