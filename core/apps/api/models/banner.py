from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.api.choices import BannerIdChoise


class BannerModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("title"), max_length=255)
    description = models.TextField(verbose_name=_("description"))
    image = models.ImageField(verbose_name=_("image"), upload_to="banners/")
    link = models.URLField(verbose_name=_("link"), max_length=255)
    position = models.CharField(verbose_name=_("position"), max_length=255, choices=BannerIdChoise)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            title="mock",
            description="mock",
            image="resources/static/images/default_avatar.jpg",
            position=BannerIdChoise.BANNER1,
            link="https://example.com/"
        )

    class Meta:
        db_table = "banner"
        verbose_name = _("BannerModel")
        verbose_name_plural = _("BannerModels")
