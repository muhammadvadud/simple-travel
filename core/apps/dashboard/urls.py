from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmployeesViewSet, TourAgencyViewSet, UsersView, TicketsViewSet

router = DefaultRouter()
router.register("users", UsersView, basename="dashboard-users")
router.register("tour-agency", TourAgencyViewSet, basename="dashboard-tour-agency")
router.register("employees", EmployeesViewSet, basename="employees")
router.register("dashboard-tickets", TicketsViewSet, basename="dashboard-tickets")
urlpatterns = [path("", include(router.urls))]
