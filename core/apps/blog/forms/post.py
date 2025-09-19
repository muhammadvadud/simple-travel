from django import forms

from core.apps.blog.models import CategoryModel, PostimagesModel, PostModel, TagModel


class PostForm(forms.ModelForm):

    class Meta:
        model = PostModel
        fields = "__all__"


class TagForm(forms.ModelForm):

    class Meta:
        model = TagModel
        fields = "__all__"


class CategoryForm(forms.ModelForm):

    class Meta:
        model = CategoryModel
        fields = "__all__"


class PostimagesForm(forms.ModelForm):

    class Meta:
        model = PostimagesModel
        fields = "__all__"
