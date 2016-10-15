from django import forms
from .models import Book
from modules.books_preferences.models import BookPreferences

CATEGORIES_CHOICES=(('TST','Terror/Suspenso/Thriller'),('AAS','Acción/Aventura'),('TEC','Tecnología/Educación'),('HOM','Hogar'),('CUL','Cultura'),('DRA','Drama'),('COM','Comedia'))
ACTIONS_CHOICES =(('SEL','Vender'),('LEN','Prestar'),('GAW','Regalar'),('REN','Rentar'),('INT','Intercambiar'))

class BookRegister(forms.Form):

	title = forms.CharField(max_length=70)
	author = forms.CharField(max_length=200)
	description = forms.CharField(widget=forms.Textarea)
	edition = forms.CharField(max_length=20)
	cover_image = forms.ImageField()
	book_images = forms.ImageField()	
	categories = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices = CATEGORIES_CHOICES)
	action_tags = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices = ACTIONS_CHOICES)	
	status = forms.BooleanField()	


class SearchBook(forms.Form):

	title = forms.CharField(max_length=70)
	author = forms.CharField(max_length=200)

""" HERE WE SHOULD OBTAIN INITIAL VALUES FROM FUNCTIONS
class InitialBookValues(forms.Form):
	class Meta:
		model = Book
		fields = ('title','author')
		widgets = {
			'title': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder': 'Nombre del libro'
			}),
			'author': forms.TextInput(attrs={
				'class': 'form-control',
				'placeholder' : 'Autor'
			})
		}

"""
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