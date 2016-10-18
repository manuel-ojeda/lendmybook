from rest_framework import serializers
from .models import BaseBook

class BookPreferencesSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = BaseBook
		fields = ('id_book','action_tags','status')
