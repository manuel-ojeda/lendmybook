from django import forms
from .models import Book
from modules.base_books.models import BaseBook

ACTIONS_CHOICES =(('SEL','Vender'),('LEN','Prestar'),('GAW','Regalar'),('REN','Rentar'),('INT','Intercambiar'))


class BookRegister(forms.Form):

	base_book = forms.ModelChoiceField(queryset=BaseBook.objects.values('title','author'))
	edition = forms.CharField(max_length=20)
	book_images = forms.ImageField()	
	action_tags = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices = ACTIONS_CHOICES)	
	status = forms.BooleanField()
	aditional_info = forms.CharField(widget=forms.Textarea)

"""
class ShowUserBooks(forms.Form):
	username = forms.CharField(
		max_length=30,
		widget=forms.TextInput(attrs={
			'class': 'form-control',
			'placeholder': 'Ingresa tu usuario'
		}))
	password = forms.CharField(
		max_length = 30,
		widget = forms.TextInput(attrs={
			'type': 'password',
			'class': 'form-control',
			'placeholder': 'Ingresa tu contraseña'
		}))
"""		