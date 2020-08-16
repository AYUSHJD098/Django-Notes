from django.forms import ModelForm, TextInput, Textarea
from .models import *

class noteForm(ModelForm):
	class Meta:
		model = note
		fields = ('title', 'note')
		widgets = {
			'title': TextInput(attrs={'class': 'form-control', 'placeholder':'title'}),
			'note': Textarea(attrs={'class': 'form-control', 'rows':'16','placeholder':'note'})
		}


