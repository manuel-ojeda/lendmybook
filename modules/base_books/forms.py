from django import forms
from .models import BaseBook

CATEGORIES_CHOICES=(('TST','Terror/Suspenso/Thriller'),('AAS','Acción/Aventura'),('TEC','Tecnología/Educación'),('HOM','Hogar'),('CUL','Cultura'),('DRA','Drama'),('COM','Comedia'))

class BaseBookRegister(forms.Form):

	title = forms.CharField(max_length=70)
	author = forms.CharField(max_length=200)
	description = forms.CharField(widget=forms.Textarea)
	cover_image = forms.ImageField()
	categories = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices = CATEGORIES_CHOICES)