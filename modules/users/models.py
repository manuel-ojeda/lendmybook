from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from modules.books.models import Book

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):


        email = self.normalize_email(email)
        if not email:
            raise ValueError('El email debe ser obligatorio')

        user = self.model(username=username, email=email,
                          is_active=True, is_staff=is_staff,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        return self._create_user(
            username, email, password, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(
            username, email, password, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    username = models.CharField(max_length=20,unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    
    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        unique_together = ('id',)

    def get_short_name(self):
        return self.username