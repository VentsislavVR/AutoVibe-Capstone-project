from cloudinary import models as cloudinary_models
from django.db import models
from django.contrib.auth import models as auth_models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from autovibe_project.accounts.managers import AutoVibeUserManager


# Create your models here.
class AutoVibeUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email already exists."),
        },
    )

    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    is_staff = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = "email"

    objects = AutoVibeUserManager()


class Profile(models.Model):
    MAX_FIRST_NAME_LENGTH = 30
    MAX_LAST_NAME_LENGTH = 30

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LENGTH,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LENGTH,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    profile_picture = cloudinary_models.CloudinaryField(
        blank=True,
        null=True,
    )
    telephone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    user = models.OneToOneField(
        AutoVibeUser,
        primary_key=True,
        on_delete=models.CASCADE,
    )

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'

        return self.first_name or self.last_name
