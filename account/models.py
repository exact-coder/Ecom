from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.utils.translation import gettext_lazy as _
# Create your models here.

class CustomUserManager(BaseUserManager):
    """Defination a model for User model with no username field"""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password"""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email, password=None, **extra_fileds):
        extra_fileds.setdefault('is_staff', False)
        extra_fileds.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fileds)

    def create_superuser(self,email, password=None, **extra_fileds):
        """Create and save a Superuser with the given email and password."""
        extra_fileds.setdefault('is_staff', True)
        extra_fileds.setdefault('is_superuser', True)

        if extra_fileds.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True')

        if extra_fileds.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True')
        return self._create_user(email, password, **extra_fileds)


# For login by Email instead of Username
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("Email Address"), max_length=254,unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    object = CustomUserManager()



    