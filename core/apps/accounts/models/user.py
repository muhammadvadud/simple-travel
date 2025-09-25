from django.contrib.auth import models as auth_models
from django.db import models
from core.apps.accounts.models.travel_agency import TravelAgency
from ..choices import RoleChoice
from ..managers import UserManager


class User(auth_models.AbstractUser):
    phone = models.CharField(max_length=255, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    avatar = models.ImageField(default="avatars/default_avatar.jpg", upload_to="avatars/")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    validated_at = models.DateTimeField(null=True, blank=True)
    travel_agency = models.ForeignKey(TravelAgency, null=True, blank=True, on_delete=models.SET_NULL)
    role = models.CharField(
        max_length=255,
        choices=RoleChoice,
        default=RoleChoice.USER,
    )

    USERNAME_FIELD = "phone"
    objects = UserManager()

    def __str__(self):
        return self.username

    @classmethod
    def _create_fake(self):
        return self.objects.create(
            phone="998940105669",
            username="mock",
        )


import math
from datetime import datetime, timedelta

from django.db import models

from django_core.models.base import AbstractBaseModel


class EmailCodeConfirm(AbstractBaseModel):
    SMS_EXPIRY_SECONDS = 120
    RESEND_BLOCK_MINUTES = 10
    TRY_BLOCK_MINUTES = 2
    RESEND_COUNT = 5
    TRY_COUNT = 10

    code = models.CharField(max_length=255)
    try_count = models.IntegerField(default=0)
    resend_count = models.IntegerField(default=0)
    email = models.EmailField()
    expire_time = models.DateTimeField(null=True, blank=True)
    unlock_time = models.DateTimeField(null=True, blank=True)
    resend_unlock_time = models.DateTimeField(null=True, blank=True)

    def sync_limits(self):
        if self.resend_count >= self.RESEND_COUNT:
            self.try_count = 0
            self.resend_count = 0
            self.resend_unlock_time = datetime.now() + timedelta(
                minutes=self.RESEND_BLOCK_MINUTES
            )
        elif self.try_count >= self.TRY_COUNT:
            self.try_count = 0
            self.unlock_time = datetime.now() + timedelta(
                minutes=self.TRY_BLOCK_MINUTES
            )

        if (
                self.resend_unlock_time is not None
                and self.resend_unlock_time.timestamp() < datetime.now().timestamp()
        ):
            self.resend_unlock_time = None

        if (
                self.unlock_time is not None
                and self.unlock_time.timestamp() < datetime.now().timestamp()
        ):
            self.unlock_time = None
        self.save()

    def is_expired(self):
        return (
            self.expire_time.timestamp() < datetime.now().timestamp()
            if hasattr(self.expire_time, "timestamp")
            else None
        )

    def is_block(self):
        return self.unlock_time is not None

    def reset_limits(self):
        self.try_count = 0
        self.resend_count = 0
        self.unlock_time = None

    def interval(self, time):
        expire = time.timestamp() - datetime.now().timestamp()
        minutes = math.floor(expire / 60)
        expire -= minutes * 60
        expire = math.floor(expire)

        return f"{minutes:02d}:{expire:02d}"

    def __str__(self) -> str:
        return f"{self.email} | {self.code}"
