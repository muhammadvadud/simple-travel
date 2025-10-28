from django_filters import rest_framework as filters

from core.apps.api.models import FaqModel, FaqCategoryModel


class FaqFilter(filters.FilterSet):
    category = filters.ModelChoiceFilter(queryset=FaqCategoryModel.objects.all(), field_name="category")

    class Meta:
        model = FaqModel
        fields = [
            "category",
        ]
