from django.db import models
from django.contrib.postgres.fields import ArrayField
from modules.users.models import User


class Preferences(models.Model):
	user_linked = models.OneToOneField(User, on_delete=models.CASCADE)
	city = models.CharField(max_length=30,blank=False)
	zones = ArrayField(models.CharField(max_length=10,blank=False))
	fav_categories = ArrayField(models.CharField(max_length=50,blank=True))
	review = models.DecimalField(max_digits=3,decimal_places=1)
	
