ss from django.db import models
from django.contrib.postgres.fields import ArrayField
from modules.books.models import Book

class BookPreferences(models.Model):

	id_book = models.OneToOneField(Book, on_delete=models.CASCADE)
	action_tags = ArrayField(models.CharField(max_length=25,blank=True),default=[])
	status = models.BooleanField(blank=False,default=False)
