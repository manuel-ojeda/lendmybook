from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

	image_url = serializers.SerializerMethodField('getBookImages')
	
	class Meta:
		model = Book
		fields = ('id_book','base_book','owner','edition','image_url','aditional_info')

	def getBookImages(self, BaseBook):
		n = str(Book.book_images.url)
		image_url = "http://lendmybook.mx"+n
		return image_url