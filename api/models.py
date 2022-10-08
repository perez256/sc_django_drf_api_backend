from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)

    # def create_user(self, email, password=None, **extra_fields):
    #
    #     if not email:
    #         raise ValueError('Email for user must be set.')
    #     email = self.normalize_email(email)
    #     user = self.model(email=email, **extra_fields)
    #
    #     if not password:
    #         raise ValueError('User must have a password')
    #
    #     user.set_password(password)
    #     user.save()
    #
    #     user.is_superuser = False
    #     user.is_staff = False
    #
    #     user.save(using=self._db)
    #     return user
    # def create_superuser(self, email, password=None, **extra_fields):
    #     # extra_fields.setdefault('is_staff', True)
    #     # extra_fields.setdefault('is_superuser', True)
    #
    #     # if extra_fields.get('is_staff') is not True:
    #     #     raise ValueError('Superuser must have is_staff=True.')
    #     # if extra_fields.get('is_superuser') is not True:
    #     #     raise ValueError('Superuser must have is_superuser=True.')
    #
    #     return self.create_superuser(email, password, **extra_fields)
    #


# Create your models here.
class User(AbstractUser):
    # username = None
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=200, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    avatar = models.ImageField(null=True, default="avatar.jpeg", blank=True)
    password = models.CharField(max_length=255, null=True, blank=True)
    is_passenger = models.BooleanField(default=False)
    is_driver = models.BooleanField(default=False)
    is_boda = models.BooleanField(default=False)
    contact = models.CharField(max_length=200, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class FeedBack(models.Model):
    bussiness_name = models.CharField(max_length=225, null=True, blank=True)
    comment = models.CharField(max_length=225, null=True, blank=True)
    contact = models.CharField(max_length=225, null=True, blank=True)
    employee_name = models.CharField(max_length=225, null=True, blank=True)
    file = models.ImageField(null=True, default="avatar.jpeg", blank=True)
    location = models.CharField(max_length=225, null=True, blank=True)
    name = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.employee_name


class ResearchLab(models.Model):
    business_name = models.CharField(max_length=225, null=True, blank=True)
    contact = models.CharField(max_length=225, null=True, blank=True)
    address = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.business_name


class Marketing(models.Model):
    name = models.CharField(max_length=225, null=True, blank=True)
    contact = models.CharField(max_length=225, null=True, blank=True)
    address = models.CharField(max_length=225, null=True, blank=True)

    def __str__(self):
        return self.name


class BookRide(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=225, null=True, blank=True)
    ride_type = models.CharField(max_length=225, null=True, blank=True)
    address_from = models.CharField(max_length=225, null=True, blank=True)
    address_to = models.CharField(max_length=225, null=True, blank=True)
    createdAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.address_to
