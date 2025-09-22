from django.contrib.auth import models as auth_models
from django.db import models

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
