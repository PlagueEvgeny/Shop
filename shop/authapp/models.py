from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator


class ProfileManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, login, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not login:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(login=login, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, login, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(login, email, password, **extra_fields)

    def create_superuser(self, login, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(login, email, password, **extra_fields)


class Profile(AbstractUser):
    objects = ProfileManager()

    username = None

    login_validator = UnicodeUsernameValidator()

    login = models.CharField(
        _('login'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[login_validator],
        error_messages={
            'unique': _("A user with that login already exists."),
        },
    )

    USERNAME_FIELD = 'login'
