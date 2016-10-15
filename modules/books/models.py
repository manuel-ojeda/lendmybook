from django.db import models

from modules.users.models import User


class Book(models.Model):	

	id_book = models.AutoField(primary_key=True)
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=70)
	author = models.CharField(max_length=200)
	description = models.TextField()
	edition = models.CharField(max_length=20)
	cover_image = models.ImageField(upload_to='../../media/cover_images/')
	isbn = models.CharField(max_length=13)
	book_images = models.ImageField(upload_to='../../media/book_images/')



class SearchBook(models.Model):	

	id_temporal = models.AutoField(primary_key=True)
	title = models.CharField(max_length=70)
	author = models.CharField(max_length=200)
	
	initialSearch = models.Manager()

"""
class ShortBook(models.Model):

	id_book = models.AutoField(primary_key=True)
	title = models.CharField(max_length=70)
	author = models.CharField(max_length=200)
	description = models.TextField()
	edition = models.TextField(max_length=20)
	cover_image = models.ImageField(upload_to='/media/cover_images')
	book_images = models.ImageField(upload_to='/media/book_images')
	categories = ArrayField(models.CharField(max_length=50,blank=False))
	action_tags = ArrayField(models.CharField(max_length=25,blank=True))
"""