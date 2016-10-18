from django.db import models
from django.conf import settings

from modules.users.models import User
from modules.base_books.models import BaseBook


class Book(models.Model):	

	id_book = models.AutoField(primary_key=True)
	base_book = models.ForeignKey(BaseBook, on_delete=models.CASCADE,default=0)
	owner = models.ForeignKey(User, on_delete=models.CASCADE,default=0)
	edition = models.CharField(max_length=20,default="1st")
	book_images = models.ImageField(upload_to=str(settings.MEDIA_URL)+'book_images/',default=str(settings.MEDIA_URL)+'default_images/default_cover.png')
	aditional_info = models.TextField(default="No info")