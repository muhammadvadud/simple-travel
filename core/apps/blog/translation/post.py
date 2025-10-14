from modeltranslation.translator import TranslationOptions, register

from core.apps.blog.models import CategoryModel, PostimagesModel, PostModel, TagModel


@register(PostModel)
class PostTranslation(TranslationOptions):
    fields = [
        "title",
        "text"
    ]


@register(TagModel)
class TagTranslation(TranslationOptions):
    fields = [
        "name"
    ]


@register(CategoryModel)
class CategoryTranslation(TranslationOptions):
    fields = [
        "name"
    ]


@register(PostimagesModel)
class PostimagesTranslation(TranslationOptions):
    fields = [
        "text"
    ]
