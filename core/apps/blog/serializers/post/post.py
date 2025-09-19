from core.apps.blog.models import PostModel
from rest_framework import serializers


class BasePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = [
            "id",
            "name",

        ]


class ListPostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta): ...


class RetrievePostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta): ...


class CreatePostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta):
        fields = [
            "id",
            "name",

        ]
