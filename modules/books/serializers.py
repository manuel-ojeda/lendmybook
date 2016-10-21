from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Book
		
"""
class NewBookSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Book
		fields = ('base_book','owner','edition','aditional_info')

"""