from django.db import models
from django.utils.translation import gettext_lazy as _
from django_core.models import AbstractBaseModel
from core.apps.accounts.models.user import User, TravelAgency
from core.apps.accounts.models.participant import ParticipantModel
from .tariff import FullTariff
from django.utils.text import slugify
from ..choices.order import OrderStatusChoices


class TransportTicketModel(AbstractBaseModel):
    name = models.CharField(verbose_name=_("name"), max_length=255)
    icon_name = models.CharField(verbose_name=_("icon name"), max_length=255)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "transport_ticket"
        verbose_name = _("TransportTicket")
        verbose_name_plural = _("TransportTicketModels")


class FullTransportInfoModel(AbstractBaseModel):
    transport = models.ForeignKey(TransportTicketModel, verbose_name=_("transport"), on_delete=models.PROTECT,
                                  related_name="full_info")
    price = models.PositiveBigIntegerField(verbose_name=_("price"), default=0)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = "transport_price"
        verbose_name = _("FullTransportInfoModel")
        verbose_name_plural = _("FullTransportInfoModels")


class TicketsModel(AbstractBaseModel):
    """Chiptalar haqidagi asosiy ma’lumotlarni saqlaydi."""
    travel_agency = models.ForeignKey(TravelAgency, related_name="tickets", on_delete=models.SET_NULL, null=True)
    title = models.CharField(verbose_name=_("title"), max_length=255)
    price = models.BigIntegerField(verbose_name=_("price"))
    min_person = models.PositiveIntegerField(verbose_name=_("min person"))
    max_person = models.PositiveIntegerField(verbose_name=_("max person"))
    departure = models.CharField(verbose_name=_("departure"), max_length=255)
    destination = models.CharField(verbose_name=_("destination"), max_length=255)
    #############
    # Bu uchalasi aniq bo'lgandan keyin yo olib tashlanadi yoki qoladi !
    departure_time = models.DateTimeField(verbose_name=_("departure time"))
    travel_time = models.DateTimeField(verbose_name=_("travel time"))
    location_name = models.CharField(
        verbose_name=_("joylashadigan manzil nomi"),
        max_length=255,
        null=True,
        blank=True
    )
    ##############
    passenger_count = models.IntegerField(verbose_name=_("passenger count"))
    languages = models.CharField(verbose_name=_("languages"), max_length=255)
    rating = models.FloatField(verbose_name=_("rating"))
    hotel_info = models.TextField(verbose_name=_("hotel info"))
    duration_days = models.IntegerField(verbose_name=_("duration days"))
    hotel_meals = models.TextField(verbose_name=_("hotel meals"), null=True, blank=True)
    tariff = models.ManyToManyField(FullTariff, related_name="ticket_tariffs", verbose_name=_("tariff"))
    slug = models.SlugField(verbose_name=_("slug"), max_length=255, unique=True, null=True, blank=True)
    badge = models.ManyToManyField("tickets.BadgeModel", verbose_name=_("badge"), null=True, blank=True)
    visa_required = models.BooleanField(verbose_name=_("visa required"))
    image_banner = models.ImageField(verbose_name=_("banner image"), upload_to="images_banner/")
    transports = models.ManyToManyField(FullTransportInfoModel, related_name="ticket_transport",
                                        verbose_name=_("transport"))
    sold_count = models.PositiveIntegerField(default=0, verbose_name=_("sold count"))
    total_income = models.PositiveBigIntegerField(default=0, verbose_name=_("total income"))
    created_at = models.DateTimeField(verbose_name=_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_("updated at"), auto_now=True)

    def __str__(self):
        return str(self.pk)

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)
        self.slug = slugify(f"{self.title}-{self.pk}")
        super().save(*args, **kwargs)

    @classmethod
    def _create_fake(self):
        from core.apps.tickets.models.badge import BadgeModel
        from django.utils.text import slugify
        import uuid

        slug = slugify(f"slug-{uuid.uuid4()}")

        ticket = self.objects.create(
            title="mock",
            price=150000,
            destination="mock",
            departure="mock",
            passenger_count=4,
            min_person=4,
            max_person=4,
            rating=4.5,
            hotel_info="mock",
            duration_days=15,
            travel_agency=TravelAgency._create_fake(),
            departure_time="2025-10-01T10:00:00",
            travel_time="2025-10-01T18:00:00",
            slug=slug,
            languages="en",
            visa_required=False,
        )

        badge = BadgeModel._create_fake()

        ticket.badge.set([badge])
        return ticket


class Meta:
    db_table = "tickets"
    verbose_name = _("TicketsModel")
    verbose_name_plural = _("TicketsModels")


class TicketsImagesModel(AbstractBaseModel):
    """Chipta bilan bog‘liq rasmlarni saqlaydi."""

    image = models.ImageField(verbose_name=_("image"), upload_to="ticket-images/")
    ticket = models.ForeignKey(
        TicketsModel, verbose_name=_("ticket"), related_name="ticket_images", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            image="resources/static/images/logo.png",
            ticket=TicketsModel._create_fake(),
        )

    class Meta:
        db_table = "tickets_images"
        verbose_name = _("TicketsImagesModel")
        verbose_name_plural = _("TicketsImagesModel")


class TicketsAmenitiesModel(AbstractBaseModel):
    """Chipta ichidagi qulayliklarni saqlaydi."""

    name = models.CharField(verbose_name=_("name"), max_length=255)
    icon_name = models.CharField(verbose_name=_("icon name"), max_length=255)
    ticket = models.ForeignKey(
        TicketsModel, verbose_name=_("ticket"), related_name="ticket_amenities", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            ticket=TicketsModel._create_fake(),
        )

    class Meta:
        db_table = "tickets_amenities"
        verbose_name = _("TicketsAmenitiesModel")
        verbose_name_plural = _("TicketsAmenitiesModel")


class TicketsIncludedServicesModel(AbstractBaseModel):
    """Chipta narxiga kiradigan xizmatlarni saqlaydi."""

    image = models.ImageField(verbose_name=_("image"), upload_to="ticket-included-services-images/")
    title = models.CharField(verbose_name=_("title"), max_length=255)
    desc = models.TextField(verbose_name=_("description"))
    ticket = models.ForeignKey(
        TicketsModel, verbose_name=_("ticket"), related_name="ticket_included_services", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            image="resources/static/images/logo.png",
            title="mock",
            desc="mock",
            ticket=TicketsModel._create_fake(),
        )

    class Meta:
        db_table = "tickets_included_services"
        verbose_name = _("TicketsIncludedServicesModel")
        verbose_name_plural = _("TicketsIncludedServicesModel")


class TicketsItineraryModel(AbstractBaseModel):
    """Chipta bo‘yicha safar rejasini saqlaydi."""

    title = models.CharField(verbose_name=_("title"), max_length=255)
    duration = models.IntegerField(verbose_name=_("duration"))
    ticket = models.ForeignKey(
        TicketsModel, verbose_name=_("ticket"), related_name="ticket_itinerary", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            title="mock",
            duration=4,
            ticket=TicketsModel._create_fake(),
        )

    class Meta:
        db_table = "tickets_itinerary"
        verbose_name = _("TicketsItineraryModel")
        verbose_name_plural = _("TicketsItineraryModel")


class TicketsItineraryImagesModel(AbstractBaseModel):
    """Safar rejasiga oid rasmlarni saqlaydi."""

    image = models.ImageField(verbose_name=_("image"), upload_to="ticket-included-services-images/")
    tickets_itinerary = models.ForeignKey(
        TicketsItineraryModel,
        verbose_name=_("tickets_itinerary"),
        related_name="ticket_itinerary_image",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            image="resources/static/images/logo.png",
            tickets_itinerary=TicketsItineraryModel._create_fake(),
        )

    class Meta:
        db_table = "tickets_itinerary_images"
        verbose_name = _("TicketsItineraryImagesModel")
        verbose_name_plural = _("TicketsItineraryImagesModel")


class TicketsItineraryDestinationsModel(AbstractBaseModel):
    """Safar davomida boriladigan manzillarni saqlaydi."""

    name = models.CharField(verbose_name=_("name"), max_length=255)
    tickets_itinerary = models.ForeignKey(
        TicketsItineraryModel,
        verbose_name=_("tickets_itinerary"),
        related_name="ticket_itinerary_destinations",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            tickets_itinerary=TicketsItineraryModel._create_fake(),
        )

    class Meta:
        db_table = "tickets_itinerary_destinations"
        verbose_name = _("TicketsItineraryDestinationsModel")
        verbose_name_plural = _("TicketsItineraryDestinationsModel")


class TicketsHotelMealsModel(AbstractBaseModel):
    """Mehmonxonada beriladigan taomlarni saqlaydi."""

    image = models.ImageField(verbose_name=_("image"), upload_to="ticket-hotel-meals/")
    name = models.CharField(verbose_name=_("name"), max_length=255)
    desc = models.TextField(verbose_name=_("description"))
    ticket = models.ForeignKey(
        TicketsModel, verbose_name=_("ticket"), related_name="ticket_hotel_meals", on_delete=models.CASCADE
    )

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            name="mock",
            desc="mock",
            ticket=TicketsModel._create_fake(),
        )

    class Meta:
        db_table = "tickets_hotel_meals"
        verbose_name = _("TicketsHotelMealsModel")
        verbose_name_plural = _("TicketsHotelMealsModel")


class TicketsCommentsModel(AbstractBaseModel):
    """Chiptaga yozilgan sharh va baholarni saqlaydi."""

    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    text = models.TextField(verbose_name=_("text"))
    rating = models.FloatField(verbose_name=_("rating"))
    ticket = models.ForeignKey(
        TicketsModel, verbose_name=_("ticket"), related_name="ticket_comments", on_delete=models.CASCADE
    )
    created = models.DateTimeField(verbose_name=_("created"), auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            user=User._create_fake(),
            text="mock",
            rating=4.5,
            tickets_itinerary=TicketsModel._create_fake(),
        )

    class Meta:
        db_table = "tickets_comments"
        verbose_name = _("TicketsCommentsModel")
        verbose_name_plural = _("TicketsCommentsModel")


class TicketorderModel(AbstractBaseModel):
    user = models.ForeignKey(User, verbose_name=_("user"), related_name="orders", on_delete=models.CASCADE)
    departure = models.CharField(verbose_name=_("departure"), max_length=255)
    destination = models.CharField(verbose_name=_("destination"), max_length=255)
    departure_date = models.DateField(verbose_name=_("departure date"))
    arrival_time = models.DateField(verbose_name=_("arrival time"))
    participant = models.ManyToManyField(ParticipantModel, verbose_name=_("participant"), null=True, blank=True)
    ticket = models.ForeignKey(TicketsModel, verbose_name=_("ticket"), on_delete=models.SET_NULL, null=True)
    tariff = models.CharField(verbose_name=_("tariff"), max_length=255)
    transport = models.CharField(verbose_name=_("transport"), max_length=255)
    extra_service = models.ManyToManyField("tickets.ExtraServicesModel", verbose_name=_("extra services"), null=True,
                                           blank=True)
    extra_paid_service = models.ManyToManyField("tickets.PaidServicesModel", verbose_name=_("extra paid services"),
                                                null=True, blank=True)
    order_status = models.CharField(verbose_name=_("order status"), max_length=255, choices=OrderStatusChoices,
                                    default=OrderStatusChoices.PENDING_PAYMENT)
    total_price = models.BigIntegerField(verbose_name=_("total price"))

    def __str__(self):
        return str(self.pk)

    @classmethod
    def _create_fake(self):
        from core.apps.tickets.models.extra_services import ExtraServicesModel, PaidServicesModel
        order = self.objects.create(
            user=User._create_fake(),
            departure="mock",
            destination="mock",
            departure_date="2025-12-01",
            arrival_time="2025-12-01",
            ticket=TicketsModel._create_fake(),
            tariff="mock",
            transport="mock",
            total_price=40,
        )
        participant = ParticipantModel._create_fake()
        extra_service = ExtraServicesModel._create_fake()
        extra_paid_service = PaidServicesModel._create_fake()

        order.participant.set([participant])
        order.extra_service.set([extra_service])
        order.extra_paid_service.set([extra_paid_service])
        return order

    class Meta:
        db_table = "ticketorder"
        verbose_name = _("TicketorderModel")
        verbose_name_plural = _("TicketorderModels")
