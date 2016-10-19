from django import forms
from .models import Preferences

CATEGORIES_CHOICES = (("TST",'Terror/Suspenso/Thriller'),('AAS','Acción/Aventura'),('TEC','Tecnología/Educación'),('HOM','Hogar'),('CUL','Cultura'),('DRA','Drama'),('COM','Comedia'))
DELEGATIONS_CHOICES = (('ALO',"Álvaro Obregón"),('AZC',"Azcapotzalco"),('BEJ',"Benito Juárez"),('CUA',"Cuajimalpa"),('COY',"Coyoacán"),('CUH',"Cuauhtémoc"),('GAM',"Gustavo A. Madero"),('IZT',"Iztacalco"),('IZP',"Iztapalapa"),('MAG',"Magdalena Contreras"),('MIH',"Miguel Hidalgo"),('MIA',"Milpa Alta"),('TLA',"Tláhuac"),('TLP',"Tlalpan"),('VEN',"Venustiano Carranza"),('XOC',"Xochimilco"))

class UserPreferencesForm(forms.Form):

	description = forms.CharField(widget=forms.Textarea)

	city = forms.CharField(required=True,
		max_length=30,
		widget=forms.TextInput())

	zones = forms.MultipleChoiceField(required=True,
		widget=forms.CheckboxSelectMultiple,
		choices = DELEGATIONS_CHOICES)

	fav_categories = forms.MultipleChoiceField(required=False,
		widget=forms.CheckboxSelectMultiple,
		choices = CATEGORIES_CHOICES)


	review = models.DecimalField(max_value=10.0,min_value=0.0)
	

