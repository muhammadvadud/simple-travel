from core.apps.blog.models import PostModel, PostimagesModel, TagModel
from rest_framework import serializers
from core.apps.blog.serializers.post.tag import BaseTagSerializer
from core.apps.blog.models.post import CategoryModel
from core.apps.blog.serializers.post.category import BaseCategorySerializer


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = ['id']


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostimagesModel
        fields = ["id", "image", "text"]


class BasePostSerializer(serializers.ModelSerializer):
    post_images = PostImagesSerializer(many=True, read_only=True)
    post_tags = BaseTagSerializer(many=True, read_only=True)

    class Meta:
        model = PostModel
        fields = [
            "id",
            "title",
            "image",
            "text",
            "post_images",
            "post_tags",
            "is_public",
            "slug",
            "created",
        ]


class ListPostSerializer(BasePostSerializer):
    short_text = serializers.SerializerMethodField()
    short_title = serializers.SerializerMethodField()
    category = BaseCategorySerializer(read_only=True)

    class Meta(BasePostSerializer.Meta):
        fields = [
            'id',
            "short_title",
            'slug',
            'image',
            'image',
            'category',
            'short_text',
            'created',
        ]

    def get_short_title(self, obj):
        return " ".join(obj.title.split()[:4]) + "..."

    def get_short_text(self, obj):
        return " ".join(obj.text.split()[:5]) + "..."


class RetrievePostSerializer(BasePostSerializer):
    class Meta(BasePostSerializer.Meta): ...


class CreatePostSerializer(BasePostSerializer):
    post_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    post_text = serializers.ListField(child=serializers.CharField(), write_only=True)
    post_tags = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = PostModel
        fields = [
            "id",
            "title",
            "image",
            "text",
            "post_images",
            "post_tags",
            "category",
            "slug",
            "created",
            "post_text"

        ]

    def validate(self, data):
        if len(data['post_images']) != len(data['post_text']):
            raise serializers.ValidationError(
                detail={"post_text": "image teng emas"}
            )
        return data

    def create(self, validated_data):
        post_images = validated_data.pop("post_images", [])
        texts = validated_data.pop("post_text", [])
        post_tags = validated_data.pop("post_tags", [])
        post = PostModel.objects.create(**validated_data)
        if post_images:
            for image in post_images:
                PostimagesModel.objects.create(post=post, image=image, text=texts.pop(0))
        if post_tags:
            for tag in post_tags:
                TagModel.objects.create(post=post, name=tag)
        return post


class UpdatePostSerializer(BasePostSerializer):
    post_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    post_text = serializers.ListField(child=serializers.CharField(), write_only=True)
    post_tags = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = PostModel
        fields = [
            "id",
            "title",
            "image",
            "text",
            "post_images",
            "post_tags",
            "category",
            "is_public",
            "slug",
            "created",
            "post_text"

        ]

    def validate(self, data):
        post_images = data.get('post_images')
        post_text = data.get('post_text')
        if post_images is not None and post_text is not None:
            if len(data['post_images']) != len(data['post_text']):
                raise serializers.ValidationError(
                    detail={"post_text": "image teng emas"}
                )
        return data
    def update(self, instance, validated_data):
        post_images = validated_data.pop("post_images", None)
        texts = validated_data.pop("post_text", None)
        post_tags = validated_data.pop("post_tags", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if post_images is not None:
            instance.post_images.all().delete()
            for idx, image in enumerate(post_images):
                text = texts[idx] if texts and idx < len(texts) else None
                PostimagesModel.objects.create(post=instance, image=image, text=text)

        if post_tags is not None:
            instance.post_tags.all().delete()
            for tag in post_tags:
                TagModel.objects.create(post=instance, name=tag)

        return instance
