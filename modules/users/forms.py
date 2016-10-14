from django import forms
from .models import User

class UserRegisterForm(forms.Form):

	username = forms.CharField(
		max_length=30,
		widget =  forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Ingresa un nombre de usuario'
	}))

	first_name = forms.CharField(
		max_length=30,
		widget =  forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Ingresa tu nombre'
	}))

	last_name = forms.CharField(
		max_length=30,
		widget =  forms.TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Ingresa tus apellidos'
	}))

	email = forms.CharField(
		max_length=30,
		widget =  forms.TextInput(attrs={
		'type': 'email',
		'placeholder': 'Ingresa tu email'
	}))

	password = forms.CharField(
		max_length=30,
		widget =  forms.TextInput(attrs={
		'class': 'form-control',
		'type': 'password',
		'placeholder': 'Ingresa una contraseña'
	}))

	birth_date = forms.DateField(
		widget = forms.TextInput(attrs={
		'class': 'form-control input-md',
		'placeholder' : 'Ingresa tu fecha de nacimiento en aaaa/mm/dd'
	}))

class LoginForm(forms.Form):
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