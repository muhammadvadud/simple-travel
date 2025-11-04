from datetime import datetime

from core.services import sms
from django.contrib.auth import get_user_model, hashers
from django.utils.translation import gettext as _
from django_core import exceptions
from rest_framework import exceptions as exc
from rest_framework.exceptions import PermissionDenied
from rest_framework_simplejwt import tokens


class UserService(sms.SmsService):
    def get_token(self, user):
        refresh = tokens.RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def create_user(self, phone):
        user, created = get_user_model().objects.update_or_create(
            phone=phone,
            defaults={
                "phone": phone,
            },
        )

        if created or not user.has_usable_password():
            user.set_unusable_password()
            user.save()

    def email_create_user(self, email):
        user, created = get_user_model().objects.update_or_create(
            email=email,
            defaults={
                "email": email,
            },
        )

        if created or not user.has_usable_password():
            user.set_unusable_password()
            user.save()

    def send_confirmation(self, phone, lang='uz') -> bool:
        try:
            self.send_confirm(phone, lang)

            return True
        except exceptions.SmsException as e:
            raise PermissionDenied(_("Qayta sms yuborish uchun kuting: {}").format(e.kwargs.get("expired")))
        except Exception:
            raise PermissionDenied(_("Serverda xatolik yuz berdi"))

    def validate_user(self, user) -> dict:
        """
        Create user if user not found
        """
        if user.validated_at is None:
            user.validated_at = datetime.now()
        user.save()
        token = self.get_token(user)
        return token

    def is_validated(self, user) -> bool:
        """
        User is validated check
        """
        if user.validated_at is not None:
            return True
        return False

    def change_password(self, phone, password):
        """
        Change password
        """
        user = get_user_model().objects.filter(phone=phone).first()
        user.set_password(password)
        user.save()

    def change_password_email(self, email, password):
        """
        Change password Email
        """
        user = get_user_model().objects.filter(email=email).first()
        user.set_password(password)
        user.save()

    def set_password_phone(self, phone, password):
        """
        Set password
        """
        user = get_user_model().objects.filter(phone=phone).first()
        if not user:
            raise exc.NotFound("User not found")

        if user.has_usable_password():
            raise exc.ValidationError("Parol allaqachon o‘rnatilgan")

        user.set_password(password)
        user.save()

    def set_password_email(self, email, password):
        """
        Set password
        """
        user = get_user_model().objects.filter(email=email).first()
        if not user:
            raise exc.NotFound("User not found")

        if user.has_usable_password():
            raise exc.ValidationError("Parol allaqachon o‘rnatilgan")

        user.set_password(password)
        user.save()

    def send_email_confirmation(self, email) -> bool:
        try:
            self.send_email_confirmation_code(email)
            return True
        except exceptions.SmsException as e:
            raise PermissionDenied(_("Qayta cod  yuborish uchun kuting: {}").format(e.kwargs.get("expired")))
        except Exception:
            raise PermissionDenied(_("Serverda xatolik yuz berdi"))
