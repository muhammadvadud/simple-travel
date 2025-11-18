from rest_framework import serializers
from core.apps.blog.models import TagModel, PostModel, CategoryModel, PostimagesModel


class DashboardPostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostimagesModel
        fields = [
            "id",
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


class TagWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagModel
        fields = [
            "id",
            "name",
            "name_ru",
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = [
            "id",
            "name",
            "name_ru",
            "name_uz",
        ]


class BaseDashboardPostSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    post_tags = TagSerializer(many=True, read_only=True)
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
            "post_tags",
            "post_images",
        ]


class ListDashboardPostSerializer(BaseDashboardPostSerializer):
    class Meta(BaseDashboardPostSerializer.Meta):
        ref_name = "ListDashboardPost"


class RetrieveDashboardPostSerializer(BaseDashboardPostSerializer):
    class Meta(BaseDashboardPostSerializer.Meta): ...


class CreateDashboardPostSerializer(BaseDashboardPostSerializer):
    post_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    post_text = serializers.ListField(child=serializers.CharField(), write_only=True, required=False)
    post_text_ru = serializers.ListField(child=serializers.CharField(), write_only=True, required=False)
    post_tags = TagWriteSerializer(many=True, write_only=True, required=False)
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
            "category",
            "post_images",
            "post_tags",
            "post_text",
            "post_text_ru",
        ]

    def validate(self, data):
        post_images = data.get('post_images', [])
        post_text = data.get('post_text', [])

        if (len(post_images) != len(post_text)):
            raise serializers.ValidationError(
                detail={"post_text": "image, text va text_ru uzunligi teng bo‘lishi kerak"}
            )
        return data

    def create(self, validated_data):
        post_images = validated_data.pop("post_images", [])

        texts = validated_data.pop("post_text", [])
        texts_ru = validated_data.pop("post_text_ru", [])
        post_tags = validated_data.pop("post_tags", [])
        post = PostModel.objects.create(**validated_data)
        if post_images:
            for image in post_images: PostimagesModel.objects.create(post=post, image=image, text=texts.pop(0),
                                                                     text_ru=texts_ru.pop(0))
        if post_tags:
            TagModel.objects.bulk_create(
                [TagModel(post=post, **tags) for tags in post_tags]
            )
        return post


class UpdateItemWriteSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField(required=False, allow_blank=True)
    text_ru = serializers.CharField(required=False, allow_blank=True)
    image = serializers.ImageField(required=False)


class UpdateDashboardPostSerializer(BaseDashboardPostSerializer):
    post_images = serializers.ListField(
        child=serializers.ImageField(),
        write_only=True,
        required=False
    )
    post_text = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
    )
    post_text_ru = serializers.ListField(
        child=serializers.CharField(),
        write_only=True,
        required=False
    )

    updates = UpdateItemWriteSerializer(many=True, write_only=True, required=False)

    delete_list = serializers.ListField(
        child=serializers.IntegerField(),
        write_only=True,
        required=False
    )
    category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all(), write_only=True, required=False)
    post_tags = TagWriteSerializer(many=True, write_only=True, required=True)

    class Meta:
        model = PostModel
        fields = [
            "id",
            "title",
            "image",
            "text",
            "category",
            "slug",
            "created",

            "post_images",
            "post_text",
            "post_text_ru",

            "updates",
            "delete_list",

            "post_tags",
            "is_public",
        ]

    def validate(self, data):
        imgs = data.get("post_images")
        txt = data.get("post_text")
        txt_ru = data.get("post_text_ru")

        if imgs is not None:
            if txt is None or txt_ru is None:
                raise serializers.ValidationError(
                    {"post_text": "text va text_ru majburiy (rasm qo‘shilayotganda)"}
                )

            if not (len(imgs) == len(txt) == len(txt_ru)):
                raise serializers.ValidationError(
                    {"post_text": "image, text, text_ru uzunliklari teng bo‘lishi kerak!"}
                )

        return data

    def update(self, instance, validated_data):
        new_images = validated_data.pop("post_images", None)
        new_texts = validated_data.pop("post_text", None)
        new_texts_ru = validated_data.pop("post_text_ru", None)
        post_tags = validated_data.pop("post_tags", None)

        updates = validated_data.pop("updates", None)
        delete_ids = validated_data.pop("delete_list", None)

        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        if delete_ids:
            PostimagesModel.objects.filter(
                post=instance,
                id__in=delete_ids
            ).delete()

        if updates:
            for item in updates:
                img_id = item.get("id")
                if not img_id:
                    continue

                try:
                    obj = PostimagesModel.objects.get(id=img_id, post=instance)
                except PostimagesModel.DoesNotExist:
                    continue

                if "text" in item:
                    obj.text = item["text"]

                if "text_ru" in item:
                    obj.text_ru = item["text_ru"]

                if "image" in item:
                    obj.image = item["image"]

                obj.save()

        if new_images:
            for img, txt, txt_ru in zip(new_images, new_texts, new_texts_ru):
                PostimagesModel.objects.create(
                    post=instance,
                    image=img,
                    text=txt,
                    text_ru=txt_ru
                )
        if post_tags:
            instance.post_tags.all().delete()
            TagModel.objects.bulk_create(
                [TagModel(post=instance, **tags) for tags in post_tags]
            )
        return instance
