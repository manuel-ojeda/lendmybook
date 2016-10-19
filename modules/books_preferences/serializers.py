from rest_framework import serializers
from .models import BookPreferences

class BookPreferencesSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = BookPreferences
		fields = ('id_book','action_tags','status')
