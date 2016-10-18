from rest_framework import serializers
from .models import BaseBook

class BaseBookSerializer(serializers.ModelSerializer):

	image_url = serializers.SerializerMethodField('getCoverImage')
	
	class Meta:
		model = BaseBook
		fields = ('id_base_book','title','author','description','image_url','isbn','categories')

	def getCoverImage(self, BaseBook):
		n = str(BaseBook.cover_image)
		image_url = "http://www.lendmybook"+n
		return image_url
