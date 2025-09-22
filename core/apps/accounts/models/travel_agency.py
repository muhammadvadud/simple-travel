from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel


class TravelAgency(AbstractBaseModel):
    STATUS_CHOICES = [
        ("pending", "Kutilmoqda"),
        ("approved", "Tasdiqlangan"),
        ("cancelled", "Bekor qilingan"),
    ]

    status = models.CharField(
        max_length=255,
        choices=STATUS_CHOICES,
        default="pending",
        verbose_name=_("status"),
    )
    share_percentage = models.IntegerField(default=0, verbose_name=_("share percentage"))
    name = models.CharField(max_length=255, verbose_name=_('TravelAgency Name'))
    addres = models.CharField(max_length=255, verbose_name=_('TravelAgency Addres'))
    email = models.EmailField(verbose_name=_('TravelAgency Email'))
    phone = models.CharField(max_length=255, verbose_name=_('TravelAgency Phone'))
    instagram = models.CharField(max_length=255, verbose_name=_('TravelAgency Instagram'), null=True, blank=True)
    web_site = models.URLField(verbose_name=_('TravelAgency Website'))

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            addres="mock",
            email="emil@email.com",
            phone="998940105669",
            instagram="@username",
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
