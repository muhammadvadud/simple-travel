from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ExtraServicesView, PaidServicesView, TariffView, TicketorderView
from .views.hotel import HotelView
from .views.tickets import TicketsView

router = DefaultRouter()
router.register("ticketorder", TicketorderView, basename="ticketorder")
router.register("paid_services", PaidServicesView, basename="paid_services")
router.register("extra_services", ExtraServicesView, basename="extra_services")
router.register("tariff", TariffView, basename="tariff")
router.register("tickets", TicketsView, basename="tickets")
router.register("hotels", HotelView, basename="hotel")
urlpatterns = [path("", include(router.urls))]
