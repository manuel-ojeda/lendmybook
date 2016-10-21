from django import forms
from .models import User

class UserRegisterForm(forms.Form):

	id_facebook = forms.CharField(max_length=100)
	name = forms.CharField(max_length=50)
	email = forms.EmailField(max_length=30)
	