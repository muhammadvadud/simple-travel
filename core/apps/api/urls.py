from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BannerView, FaqView, LocationViewSet

router = DefaultRouter()
router.register("locations", LocationViewSet, basename="locations")
router.register("banner", BannerView, basename="banner")
router.register("faq", FaqView, basename="faq")
urlpatterns = [path("", include(router.urls))]
