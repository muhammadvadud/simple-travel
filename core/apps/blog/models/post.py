from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from django.utils.text import slugify


class CategoryModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "category"
        verbose_name = _("CategoryModel")
        verbose_name_plural = _("CategoryModels")


class PostModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("title"), max_length=255)
    image = models.ImageField(verbose_name=_("image"), upload_to="post/images/")
    text = models.TextField(verbose_name=_("text"))
    category = models.ForeignKey(CategoryModel, related_name="post_category", verbose_name=_("category"),
                                 on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name=_("slug"), max_length=255, unique=True, null=True, blank=True)
    is_public = models.BooleanField(verbose_name=_("is public"), default=False)
    created = models.DateTimeField(verbose_name=_("created"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("updated"), auto_now=True)

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        if self.title and (not self.slug or self.slug != slugify(self.title)):
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            title="title",
            text="text",
            image="images/logo.png",
            category=CategoryModel._create_fake(),
        )

    class Meta:
        db_table = "post"
        verbose_name = _("PostModel")
        verbose_name_plural = _("PostModels")


class TagModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    post = models.ForeignKey(PostModel, verbose_name=_("post"), related_name="post_tags", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            post=PostModel._create_fake(),
        )

    class Meta:
        db_table = "tag"
        verbose_name = _("TagModel")
        verbose_name_plural = _("TagModels")


class PostimagesModel(AbstractBaseModel):
    image = models.ImageField(verbose_name=_("image"), upload_to="post/images/")
    text = models.TextField(verbose_name=_("text"), null=True, blank=True)
    post = models.ForeignKey(PostModel, verbose_name=_("post"), related_name="post_images", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            image="resources/static/images/default_avatar.jpg",
            text="mock",
            post=PostModel._create_fake(),
        )

    class Meta:
        db_table = "PostImages"
        verbose_name = _("PostimagesModel")
        verbose_name_plural = _("PostimagesModels")
