from django_filters import rest_framework as filters

from core.apps.blog.models import CategoryModel, PostimagesModel, PostModel, TagModel


class PostFilter(filters.FilterSet):
    category = filters.NumberFilter(field_name='category__id', lookup_expr='exact')

    class Meta:
        model = PostModel
        fields = [
            "category",
        ]


class TagFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = TagModel
        fields = ["name"]


class CategoryFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = CategoryModel
        fields = [
            "name",
        ]


class PostimagesFilter(filters.FilterSet):
    # name = filters.CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = PostimagesModel
        fields = [
        ]
