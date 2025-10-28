from rest_framework import serializers
from core.apps.blog.models import TagModel, PostModel, CategoryModel, PostimagesModel


class DashboardPostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostimagesModel
        fields = [
            "image",
            "text",
            "text_ru",
            "text_uz",
        ]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            "name",
            "name_ru",
            "name_uz",
        ]


class BaseDashboardPostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    tag = TagSerializer(many=True, read_only=True)
    post_images = DashboardPostImageSerializer(many=True, read_only=True)

    class Meta:
        model = PostModel
        fields = [
            "id",
            "title",
            "title_ru",
            "title_uz",
            "image",
            "text",
            "text_ru",
            "text_uz",
            "is_public",
            "category",
            "tag",
            "post_images",
        ]


class ListDashboardPostSerializer(BaseDashboardPostSerializer):
    class Meta(BaseDashboardPostSerializer.Meta):
        ref_name = "ListDashboardPost"


class RetrieveDashboardPostSerializer(BaseDashboardPostSerializer):
    class Meta(BaseDashboardPostSerializer.Meta):
        ref_name = "RetrieveDashboardPost"


class CreateDashboardPostSerializer(BaseDashboardPostSerializer):
    post_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    post_text = serializers.ListField(child=serializers.CharField(), write_only=True)
    post_text_ru = serializers.ListField(child=serializers.CharField(), write_only=True)
    post_tags = serializers.ListField(child=serializers.CharField(), write_only=True)
    category = serializers.PrimaryKeyRelatedField(
        queryset=CategoryModel.objects.all()
    )

    class Meta:
        model = PostModel
        fields = [
            "id",
            "title",
            "title_ru",
            "image",
            "text",
            "text_ru",
            "is_public",
            "category",
            "tag",
            "post_images",
            "post_tags",
            "post_text",
            "post_text_ru",
        ]
        ref_name = "CreateDashboardPost"

    def validate(self, data):
        if len(data['post_images']) != len(data['post_text']) and len(data['post_images']) != len(data['post_text_ru']):
            raise serializers.ValidationError(
                detail={"post_text": "image teng emas"}
            )
        return data

    def create(self, validated_data):
        post_images = validated_data.pop("post_images", [])
        texts = validated_data.pop("post_text", [])
        texts_ru = validated_data.pop("post_text_ru", [])
        post_tags = validated_data.pop("post_tags", [])
        post = PostModel.objects.create(**validated_data)
        if post_images:
            for image in post_images:
                PostimagesModel.objects.create(post=post, image=image, text=texts.pop(0),
                                               text_ru=texts_ru.pop(0))
        if post_tags:
            for tag in post_tags:
                TagModel.objects.create(post=post, name=tag)
        return post


class UpdateDashboardPostSerializer(BaseDashboardPostSerializer):
    post_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    post_text = serializers.ListField(child=serializers.CharField(), write_only=True)
    post_text_ru = serializers.ListField(child=serializers.CharField(), write_only=True)
    post_tags = serializers.ListField(child=serializers.CharField(), write_only=True)

    class Meta:
        model = PostModel
        fields = [
            "id",
            "title",
            "title_ru",
            "image",
            "text",
            "text_ru",
            "is_public",
            "category",
            "tag",
            "post_images",
            "post_tags",
            "post_text",
            "post_text_ru",
        ]
        ref_name = "UpdateDashboardPost"

    def validate(self, data):
        post_images = data.get('post_images')
        post_text = data.get('post_text')
        post_text_ru = data.get('post_text_ru')
        if post_images is not None and post_text is not None and post_text_ru is not None:
            if len(data['post_images']) != len(data['post_text']) and len(data['post_images']) != len(
                    data['post_text_ru']):
                raise serializers.ValidationError(
                    detail={"post_text": "image teng emas"}
                )
        return data

    def update(self, instance, validated_data):
        post_images = validated_data.pop("post_images", None)
        texts = validated_data.pop("post_text", None)
        texts_ru = validated_data.pop("post_text_ru", None)
        post_tags = validated_data.pop("post_tags", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if post_images is not None:
            instance.post_images.all().delete()
            for idx, image in enumerate(post_images):
                text = texts[idx] if texts and idx < len(texts) else None
                text_ru = texts_ru[idx] if texts_ru and idx < len(texts_ru) else None

                PostimagesModel.objects.create(
                    post=instance,
                    image=image,
                    text=text,
                    text_ru=text_ru
                )

        if post_tags is not None:
            instance.post_tags.all().delete()
            for tag in post_tags:
                TagModel.objects.create(post=instance, name=tag)

        return instance
