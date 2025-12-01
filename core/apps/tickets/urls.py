from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BadgeView, ExtraServicesView, PaidServicesView, TariffView, TicketorderView, GetOrderPdfView, \
    TicketsCommentsViewSet, CountryView
from .views.hotel import HotelView
from .views.tickets import TicketsView, GetTicketInfoOrderCreateView

router = DefaultRouter()
router.register("countries", CountryView, basename="countries")
router.register("badge", BadgeView, basename="badge")
router.register("ticketorder", TicketorderView, basename="ticketorder")
router.register("paid_services", PaidServicesView, basename="paid_services")
router.register("extra_services", ExtraServicesView, basename="extra_services")
router.register("tariff", TariffView, basename="tariff")
router.register("tickets", TicketsView, basename="tickets")
router.register("hotels", HotelView, basename="hotel")
router.register("get-ticket-info", GetTicketInfoOrderCreateView, basename="get-ticket-info")
router.register("ticket-comment", TicketsCommentsViewSet, basename="ticket-comment")
urlpatterns = [
    path("", include(router.urls)),
    path("get-order-pdf/", GetOrderPdfView.as_view(), name="get-order-pdf"),
]
