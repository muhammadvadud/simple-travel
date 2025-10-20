from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from django.conf import settings
from ..choices import ParticipantGenderChoices
from ..models.user import User


class ParticipantModel(AbstractBaseModel):
    gender = models.CharField(verbose_name=_("gender"), max_length=255, choices=ParticipantGenderChoices,
                              default='male')
    first_name = models.CharField(verbose_name=_("first name"), max_length=255)
    last_name = models.CharField(verbose_name=_("last name"), max_length=255)
    birth_date = models.DateField(verbose_name=_("birth date"))
    phone_number = models.CharField(verbose_name=_("phone number"), max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("created by"),related_name="participant", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            first_name="mock",
            last_name="mock",
            birth_date="2025-09-19",
            phone_number="998940105669",
            created_by=User._create_fake(),
        )

    class Meta:
        db_table = "participant"
        verbose_name = _("ParticipantModel")
        verbose_name_plural = _("ParticipantModels")


class ParticipantPasportImageModel(AbstractBaseModel):
    image = models.ImageField(verbose_name=_("image"), upload_to="participant_images/")
    participant = models.ForeignKey(ParticipantModel, related_name="participant_pasport_image",
                                    on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            image="resources/static/images/default_avatar.jpg",
            participant=ParticipantModel._create_fake(),
        )

    class Meta:
        db_table = "participant_pasport_image"
        verbose_name = _("ParticipantPasportImageModel")
        verbose_name_plural = _("ParticipantPasportImageModels")
