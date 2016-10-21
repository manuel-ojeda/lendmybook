from django import forms
from .models import BookPreferences
from modules.base_books.models import BaseBook

ACTIONS_CHOICES =(('SEL','Vender'),('LEN','Prestar'),('GAW','Regalar'),('REN','Rentar'),('INT','Intercambiar'))


class BookPreferencesRegister(forms.Form):

	id_book = models.OneToOneField(Book, on_delete=models.CASCADE)
	action_tags = ArrayField(models.CharField(max_length=25,blank=True),default=[])
	status = models.BooleanField(blank=False,default=False)
