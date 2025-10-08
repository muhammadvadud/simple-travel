from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class FaqCategoryModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("faq category name"), max_length=255)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
        )

    class Meta:
        db_table = "faq_category"
        verbose_name = _("FaqCategoryModel")
        verbose_name_plural = _("FaqCategoryModels")


class FaqModel(AbstractBaseModel):
    title = models.CharField(verbose_name=_("title"), max_length=255)
    text = models.TextField(verbose_name=_("text"))
    category = models.ForeignKey(FaqCategoryModel, verbose_name=_("category"), related_name="faqs",
                                 on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            title="mock",
            text="mock",
            category=FaqCategoryModel._create_fake(),
        )

    class Meta:
        db_table = "faq"
        verbose_name = _("FaqModel")
        verbose_name_plural = _("FaqModels")
