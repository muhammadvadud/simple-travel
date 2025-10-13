from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClickWebhookAPIView, PaymeCallBackAPIView

router = DefaultRouter()
urlpatterns = [
    path("", include(router.urls)),
    path("click/update/", ClickWebhookAPIView.as_view()),
    path("payme/update/", PaymeCallBackAPIView.as_view()),
]
