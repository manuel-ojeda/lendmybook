from django import forms


class BaseBookSearch(forms.Form):

	title = forms.CharField(max_length=70)
	author = forms.CharField(max_length=200


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