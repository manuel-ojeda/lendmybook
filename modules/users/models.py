from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

class UserManager(BaseUserManager, models.Manager):

    def _create_user(self, email, is_staff, is_superuser, **extra_fields):


        email = self.normalize_email(email)
        if not email:
            raise ValueError('El email debe ser obligatorio')

        user.save(using=self._db)
        return user

    def create_user(self, email, **extra_fields):
        return self._create_user(email, False, False, **extra_fields)

    def create_superuser(self, email, **extra_fields):
        return self._create_user(email, True, True, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin, models.Model):

    id_user = models.AutoField(primary_key=True)
    id_facebook = models.CharField(max_length=100,default="")
    #username = models.CharField(max_length=20,unique=True,default="")
    name = models.CharField(max_length=50,default="")
    #last_name = models.CharField(max_length=20,default="")
    email = models.EmailField(unique=True)
    #phone_number = models.CharField(max_length=15,unique=True,default="")
    #birth_date = models.DateField(null=False, blank=False,default="1998-01-01")
    
    objects = UserManager()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_short_name(self):
        return self.email