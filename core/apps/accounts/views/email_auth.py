import uuid
from typing import Type

from core.services import UserService, SmsService
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_core import exceptions
from drf_spectacular.utils import extend_schema
from rest_framework import status, throttling, request
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from rest_framework.viewsets import GenericViewSet
from django_core.mixins import BaseViewSetMixin
from rest_framework.decorators import action
from ..serializers import (
    EmailRegisterSerializer,
    EmailConfirmSerializer,
    EmailResetPasswordSerializer,
    EmailResetConfirmationSerializer,
    EmailResendSerializer,
    SetPasswordSerializer,
)

from rest_framework.permissions import AllowAny

from .. import models


@extend_schema(tags=["email_register"])
class EmailRegisterView(BaseViewSetMixin, GenericViewSet, UserService):
    throttle_classes = [throttling.UserRateThrottle]
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        match self.action:
            case "register":
                return EmailRegisterSerializer
            case "confirm":
                return EmailConfirmSerializer
            case "resend":
                return EmailResendSerializer
            case _:
                return EmailRegisterSerializer

    @action(methods=["POST"], detail=False, url_path="register")
    def register(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.data
        email = data.get("email")
        # Create pending user
        self.email_create_user(email, data.get("first_name"), data.get("last_name"), data.get("password"))
        self.send_email_confirmation(email)  # Send confirmation code for email
        return Response(
            {"detail": _("Sizning %(email)s gizga cod yuborildi yuborildi") % {"email": email}},
            status=status.HTTP_202_ACCEPTED,
        )

    @extend_schema(summary="Auth confirm.", description="Auth confirm user.")
    @action(methods=["POST"], detail=False, url_path="confirm")
    def confirm(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.data
        email, code = data.get("email"), data.get("code")
        try:
            if SmsService.check_email_confirm(email, code=code):
                token = self.validate_user(get_user_model().objects.filter(email=email).first())
                return Response(
                    data={
                        "detail": _("Tasdiqlash ko'di qabul qilindi"),
                        "token": token,
                    },
                    status=status.HTTP_202_ACCEPTED,
                )
        except exceptions.SmsException as e:
            raise PermissionDenied(e)  # Response exception for APIException
        except Exception as e:
            raise PermissionDenied(e)  # Api exception for APIException

    @action(methods=["POST"], detail=False, url_path="resend")
    def resend(self, rq: Type[request.Request]):
        ser = self.get_serializer(data=rq.data)
        ser.is_valid(raise_exception=True)
        email = ser.data.get("email")
        self.send_email_confirmation(email)
        return Response({"detail": _("Sizning %(email)s gizga cod yuborildi yuborildi") % {"email": email}})


@extend_schema(tags=["email-reset-password"])
class EmailResetPasswordView(BaseViewSetMixin, GenericViewSet, UserService):
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        match self.action:
            case "reset_password":
                return EmailResetPasswordSerializer
            case "reset_confirm":
                return EmailResetConfirmationSerializer
            case "reset_password_set":
                return SetPasswordSerializer
            case _:
                return None

    @action(methods=["POST"], detail=False, url_path="reset-password")
    def reset_password(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        email = ser.data.get("email")
        self.send_email_confirmation(email)
        return Response({"detail": _("Email %(email)s ga yuborildi") % {"email": email}})
    ####

    @action(methods=["POST"], detail=False, url_path="reset-password-confirm")
    def reset_confirm(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)

        data = ser.data
        code, email = data.get("code"), data.get("phone")
        try:
            SmsService.check_email_confirm(email, code)
            token = models.ResetToken.objects.create(
                user=get_user_model().objects.filter(email=email).first(),
                token=str(uuid.uuid4()),
            )
            return Response(
                data={
                    "token": token.token,
                    "created_at": token.created_at,
                    "updated_at": token.updated_at,
                },
                status=status.HTTP_200_OK,
            )
        except exceptions.SmsException as e:
            raise PermissionDenied(str(e))
        except Exception as e:
            raise PermissionDenied(str(e))

    @action(methods=["POST"], detail=False, url_path="reset-password-set")
    def reset_password_set(self, request):
        ser = self.get_serializer(data=request.data)
        ser.is_valid(raise_exception=True)
        data = ser.data
        token = data.get("token")
        password = data.get("password")
        token = models.ResetToken.objects.filter(token=token)
        if not token.exists():
            raise PermissionDenied(_("Invalid token"))
        email = token.first().user.email
        token.delete()
        self.change_password(email, password)
        return Response({"detail": _("password updated")}, status=status.HTTP_200_OK)



