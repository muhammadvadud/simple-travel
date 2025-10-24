from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from ..choices.travel_agency import TravelAgencyStatusChoices


class TravelAgency(AbstractBaseModel):
    status = models.CharField(
        max_length=255,
        choices=TravelAgencyStatusChoices,
        default=TravelAgencyStatusChoices.PENDING,
        verbose_name=_("status"),
    )
    custom_id = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=_("custom id"),
        blank=True,
    )
    share_percentage = models.IntegerField(default=0, verbose_name=_("share percentage"))
    name = models.CharField(max_length=255, verbose_name=_('TravelAgency Name'))
    addres = models.CharField(max_length=255, verbose_name=_('TravelAgency Addres'))
    email = models.EmailField(verbose_name=_('TravelAgency Email'))
    phone = models.CharField(max_length=255, verbose_name=_('TravelAgency Phone'))
    web_site = models.URLField(verbose_name=_('TravelAgency Website'))
    ticket_sold_count = models.PositiveIntegerField(default=0, verbose_name=_("ticket sold count"))
    total_income = models.PositiveBigIntegerField(default=0, verbose_name=_("total income"))

    def save(self, *args, **kwargs):
        if not self.id:
            super().save(*args, **kwargs)
            self.custom_id = f"T-100{self.id}"
            return super().save(update_fields=["custom_id"])
        else:
            return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.name)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            addres="mock",
            email="emil@email.com",
            phone="998940105669",
            web_site="http://test.com",
        )

    class Meta:
        db_table = "travel_agency"
        verbose_name = _("TravelAgency")
        verbose_name_plural = _("TravelAgencies")


class TravelAgencyDocuments(AbstractBaseModel):
    file = models.FileField(verbose_name=_('TravelAgencyDocuments File'), upload_to="travel_agency_documents/")
    travel_agency = models.ForeignKey(TravelAgency, verbose_name=_('travel_agency'),
                                      related_name="travel_agency_documents", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            file="test.py",
            travel_agency=TravelAgency._create_fake(),
        )

    class Meta:
        db_table = "travel_agency_document"
        verbose_name = _("TravelAgencyDocument")
        verbose_name_plural = _("TravelAgencyDocuments")
