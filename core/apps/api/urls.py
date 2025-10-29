from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import BannerView, FaqView

router = DefaultRouter()
router.register("banner", BannerView, basename="banner")
router.register("faq", FaqView, basename="faq")
urlpatterns = [path("", include(router.urls))]
