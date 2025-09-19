from django.contrib import admin
from unfold.admin import ModelAdmin

from core.apps.blog.models import CategoryModel, PostimagesModel, PostModel, TagModel


@admin.register(PostModel)
class PostAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(TagModel)
class TagAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(CategoryModel)
class CategoryAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )


@admin.register(PostimagesModel)
class PostimagesAdmin(ModelAdmin):
    list_display = (
        "id",
        "__str__",
    )
