from django_core.models.base import AbstractBaseModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError


class SiteSettings(AbstractBaseModel):
    address = models.TextField(verbose_name=_('Address'))
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name=_('Latitude'))
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name=_('Longitude'))
    telegram = models.CharField(verbose_name=_('Telegram'), max_length=255, blank=True, null=True)
    telegram_chat = models.CharField(verbose_name=_('Telegram'), max_length=255, blank=True, null=True)
    instagram = models.CharField(verbose_name=_('Instagram'), max_length=255, blank=True, null=True)
    facebook = models.CharField(verbose_name=_('Facebook'), max_length=255, blank=True, null=True)
    twitter = models.CharField(verbose_name=_('Twitter'), max_length=255, blank=True, null=True)
    linkedin = models.CharField(verbose_name=_('Linkedin'), max_length=255, blank=True, null=True)
    email = models.EmailField(verbose_name=_('Email'), blank=True, null=True)
    main_phone = models.CharField(verbose_name=_('Main Phone'), max_length=255, blank=True, null=True)
    other_phone = models.CharField(verbose_name=_('Other Phone'), max_length=255, blank=True, null=True)

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        if not self.pk and SiteSettings.objects.exists():
            raise ValidationError("Faqat bitta SiteSettings yozuvi bo‘lishi mumkin.")
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'site_settings'
        verbose_name = _('Site Settings')
        verbose_name_plural = _('Site Settings')


class SiteSeo(AbstractBaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    description = models.TextField(verbose_name=_('Description'))
    keywords = models.TextField(verbose_name=_('Keywords'))
    og_title = models.CharField(verbose_name=_('Og Title'), max_length=255)
    og_description = models.TextField(verbose_name=_('Og Description'))
    og_image = models.ImageField(verbose_name=_('Og Image'), upload_to='site_settings/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk and SiteSeo.objects.exists():
            raise ValidationError("Faqat bitta Seo yozuvi bo‘lishi mumkin.")
        super().save(*args, **kwargs)

    class Meta:
        db_table = 'site_seo'
        verbose_name = _('Site Seo')
        verbose_name_plural = _('Site Seo')
