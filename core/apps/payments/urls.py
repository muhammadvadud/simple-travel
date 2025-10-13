from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ClickWebhookAPIView, PaymeCallBackAPIView, PaymentLinkView

router = DefaultRouter()
urlpatterns = [
    path("", include(router.urls)),
    path("click/update/", ClickWebhookAPIView.as_view()),
    path("payme/update/", PaymeCallBackAPIView.as_view()),
    path("payments_link/<str:payment_type>/", PaymentLinkView.as_view()),
]
