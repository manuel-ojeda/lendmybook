from django.db import models
from django.contrib.postgres.fields import ArrayField
from modules.users.models import User
from modules.books.models import Book

class Event(models.Model):

	id_event = models.AutoField(primary_key=True)
	id_owner = models.ForeignKey(User, on_delete=models.CASCADE,related_name="owner")
	id_client = models.ForeignKey(User, on_delete=models.CASCADE,related_name="client")
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	transaction_type = models.CharField(max_length=3,default="")
	date = models.DateField(null=False,blank=False)
	place = models.CharField(max_length=3,default="")

