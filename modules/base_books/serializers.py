from rest_framework import serializers
from .models import BaseBook

class BaseBookSerializer(serializers.ModelSerializer):

	class Meta:
		model = BaseBook