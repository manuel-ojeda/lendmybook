from django import forms
from .models import User

class UserRegisterForm(forms.Form):

	username = forms.CharField(
		max_length=30,
		widget = forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Ingresa un nombre de usuario'
	}))

	first_name = forms.CharField(
		max_length=30,
		widget = forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Ingresa tu nombre'
	}))

	last_name = forms.CharField(
		max_length=30,
		widget = forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Ingresa tus apellidos'
	}))

	email = forms.CharField(
		max_length=30,
		widget = forms.TextInput(attrs={
		'type': 'email',
		'placeholder': 'Ingresa tu email'
	}))

	phone_number = forms.CharField(
		max_length=15,
		widget = forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Numero de telefono'
	}))

	birth_date = forms.DateField(
		widget = forms.TextInput(attrs={
		'class': 'form-control input-md',
		'placeholder' : 'Ingresa tu fecha de nacimiento en aaaa/mm/dd'
	}))

	description = forms.CharField(
		widget = forms.Textarea(atts={
		'class':'form-control',
		'placeholder': 'Ingresa una breve descripcion'
	}))

class LoginForm(forms.Form):
	username = forms.CharField(
		max_length=30,
		widget= forms.TextInput(attrs={
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