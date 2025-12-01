from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmployeesViewSet, TourAgencyViewSet, UsersView, TicketsViewSet, TicketBadgeViewSet, \
    TicketTariffViewSet, TicketTransportViewSet, HotelTypeViewSet, HotelViewSet, TicketOrderViewSet, PostView, \
    CategoryViewSet, FaqViewSet, FaqCategoryViewSet, SupportViewSet, TravelAgencyRequestViewSet, HotelFeatureViewSet, \
    HotelFeatureTypeViewSet, SiteSettingsViewSet, SiteSeoViewSet, OffertaViewSet, HelpPageViewSet, \
    UpdateFeaturedTicketAPIView, BannerViewSet, TravelAgencyReportViewSet, TravelAgencyPaymentsViewSet, \
    TourAdminViewSet, TicketAmenitiesViewSet, OrderStatusHistoryPaymentsViewSet, TravelAgencyPayOutRequestViewSet, \
    CountryViewSet, RegionViewSet

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
router.register("dashboard-faq", FaqViewSet, basename="dashboard-faq")
router.register("dashboard-faq-category", FaqCategoryViewSet, basename="dashboard-faq-category")
router.register("dashboard-support", SupportViewSet, basename="dashboard-support")
router.register("dashboard-ticket-hotel-feature", HotelFeatureViewSet, basename="dashboard-ticket-hotel-feature")
router.register("dashboard-site-settings", SiteSettingsViewSet, basename="dashboard-site-settings")
router.register("dashboard-site-seo", SiteSeoViewSet, basename="dashboard-site-seo")
router.register("dashboard-site-offerta", OffertaViewSet, basename="dashboard-site-offerta")
router.register("dashboard-site-help-page", HelpPageViewSet, basename="dashboard-site-help-page")
router.register("dashboard-site-banner", BannerViewSet, basename="dashboard-site-banner")
router.register("dashboard-site-agency-payments", TravelAgencyPaymentsViewSet,
                basename="dashboard-site-agency-payments")
router.register("dashboard-site-travel-agency-report", TravelAgencyReportViewSet,
                basename="dashboard-site-travel-agency-report")
router.register("dashboard-ticket-hotel-feature-type", HotelFeatureTypeViewSet,
                basename="dashboard-ticket-hotel-feature-type")
router.register("dashboard-travel-agency-request", TravelAgencyRequestViewSet,
                basename="dashboard-travel-agency-request")
router.register("dashboard-tickets-settings-transport", TicketTransportViewSet,
                basename="dashboard-tickets-settings-transport")
router.register("dashboard-tickets-settings-hotel-type", HotelTypeViewSet,
                basename="dashboard-tickets-settings-hotel-type")
router.register("dashboard-tour-admin", TourAdminViewSet,
                basename="dashboard-tour-admin")
router.register("dashboard-ticket-settings-amenities", TicketAmenitiesViewSet,
                basename="dashboard-ticket-settings-amenities")
router.register("dashboard-order-status-history", OrderStatusHistoryPaymentsViewSet,
                basename="dashboard-order-status-history")
router.register("dashboard-agency-payout-request", TravelAgencyPayOutRequestViewSet,
                basename="dashboard-agency-payout-request")
router.register("dashboard-ticket-settings-country", CountryViewSet,
                basename="dashboard-ticket-settings-country")
router.register("dashboard-ticket-settings-region", RegionViewSet,
                basename="dashboard-ticket-settings-region")

urlpatterns = [
    path("", include(router.urls)),
    path("dashboard-ticket-featured/<int:id>/<int:value>/", UpdateFeaturedTicketAPIView.as_view(),
         name="dashboard-ticket-featured"),

]
