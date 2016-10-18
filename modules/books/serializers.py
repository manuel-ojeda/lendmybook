from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):

	image_url = serializers.SerializerMethodField('getCoverImage')
	
	class Meta:
		model = Book
		fields = ('id_book','base_book','owner','edition','image_url','aditional_info')

	def getCoverImage(self, BaseBook):
		n = str(Book.book_images)
		image_url = "http://www.lendmybook"+n
		return image_url