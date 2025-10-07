from .views import ParticipantView, SupportView

"""
Accounts app urls
"""
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from .views import (
    ChangePasswordView,
    EmailRegisterView,
    EmailResetPasswordView,
    MeView,
    RegisterView,
    ResetPasswordView,
    EmailTokenObtainPairView,
    TravelAgencyView,
    PhoneTokenObtainPairView
)
from .views.likes import LikesView

router = DefaultRouter()
router.register("support", SupportView, basename="support")
router.register("participant", ParticipantView, basename="participant")
router.register("auth", RegisterView, basename="auth")
router.register("auth", ResetPasswordView, basename="reset-password")
router.register("auth", MeView, basename="me")
router.register("auth", ChangePasswordView, basename="change-password")
router.register("likes", LikesView, basename="likes")
router.register("email-auth", EmailRegisterView, basename="email-auth")
router.register("email-auth", EmailResetPasswordView, basename="email-reset-password")
router.register("travel-agency", TravelAgencyView, basename="travel-agency")
urlpatterns = [
    path("", include(router.urls)),
    path("auth/token/email/", EmailTokenObtainPairView.as_view(), name="token_obtain_email"),
    path("auth/token/phone/", PhoneTokenObtainPairView.as_view(), name="token_obtain_phone"),
    path("auth/token/verify/", jwt_views.TokenVerifyView.as_view(), name="token_verify"),
    path("auth/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
