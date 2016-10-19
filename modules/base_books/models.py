from django.db import models
from django.contrib.postgres.fields import ArrayField


class BaseBook(models.Model):	

	id_base_book = models.AutoField(primary_key=True)
	title = models.CharField(max_length=70,default="")
	author = models.CharField(max_length=200,default="")
	description = models.TextField(default="")
	cover_image = models.ImageField(upload_to='cover_images/',default='default_images/default_cover.png')
	isbn = models.CharField(max_length=13,default="")
	categories = ArrayField(models.CharField(max_length=50,blank=False),default=[])