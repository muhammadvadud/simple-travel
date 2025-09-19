from modeltranslation.translator import TranslationOptions, register

from core.apps.blog.models import CategoryModel, PostimagesModel, PostModel, TagModel


@register(PostModel)
class PostTranslation(TranslationOptions):
    fields = []


@register(TagModel)
class TagTranslation(TranslationOptions):
    fields = []


@register(CategoryModel)
class CategoryTranslation(TranslationOptions):
    fields = []


@register(PostimagesModel)
class PostimagesTranslation(TranslationOptions):
    fields = []
