from django import forms
from .models import Event
from modules.users.models import User
from modules.books.models import Book

class EventRegister(forms.Form):

	id_event = forms.AutoField(primary_key=True)
	id_owner = forms.ForeignKey(User, on_delete=forms.CASCADE,related_name="owner")
	id_client = forms.ForeignKey(User, on_delete=forms.CASCADE,related_name="client")
	book = forms.ForeignKey(Book, on_delete=forms.CASCADE)
	transaction_type = forms.CharField(max_length=3,default="")
	date = forms.DateField(null=False,blank=False)
	place = forms.CharField(max_length=3,default="")
