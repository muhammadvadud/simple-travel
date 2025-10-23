from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmployeesViewSet, TourAgencyViewSet, UsersView, TicketsViewSet, TicketBadgeViewSet, \
    TicketTariffViewSet, TicketTransportViewSet, HotelTypeViewSet, HotelViewSet, TicketOrderViewSet, PostView, \
    CategoryViewSet

router = DefaultRouter()
router.register("users", UsersView, basename="dashboard-users")
router.register("tour-agency", TourAgencyViewSet, basename="dashboard-tour-agency")
router.register("employees", EmployeesViewSet, basename="employees")
router.register("dashboard-tickets", TicketsViewSet, basename="dashboard-tickets")
router.register("dashboard-tickets-settings-badge", TicketBadgeViewSet, basename="dashboard-tickets-settings-badge")
router.register("dashboard-tickets-settings-tariff", TicketTariffViewSet, basename="dashboard-tickets-settings-tariff")
router.register("dashboard-hotel", HotelViewSet, basename="dashboard-hotel")
router.register("dashboard-ticket-order", TicketOrderViewSet, basename="dashboard-ticket-order")
router.register("dashboard-post", PostView, basename="dashboard-post")
router.register("dashboard-category", CategoryViewSet, basename="dashboard-category")
router.register("dashboard-tickets-settings-transport", TicketTransportViewSet,
                basename="dashboard-tickets-settings-transport")
router.register("dashboard-tickets-settings-hotel-type", HotelTypeViewSet,
                basename="dashboard-tickets-settings-hotel-type")
urlpatterns = [path("", include(router.urls))]
