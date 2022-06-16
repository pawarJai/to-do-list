from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin)


# Create your models here.


class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email,and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        try:
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user
        except:
            raise
 
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
 
        return self._create_user(email, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    is_active = models.BooleanField(default=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(
        verbose_name='email address', max_length=255, unique=True,)
    phone = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def full_name(self):
        return self.name

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    @staticmethod
    def get_user_by_email(email):
        try:
            return User.objects.get(email =email)
        except:
            return False

    @staticmethod
    def get_user_by_password(password):
        try:
            return User.objects.get(password=password)
        except:
            return False