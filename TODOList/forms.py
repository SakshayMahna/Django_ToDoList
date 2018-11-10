from django.forms import ModelForm			#custom made new python file for forms
from django import forms									#finally import this to view

from .models import List


class ListForm(forms.ModelForm):
	class Meta:								#Modifying parent class
		model = List
		fields = ['MEMO', 'CONDITION', 'NUMBER']		#AUTHOR should not be present here as it is a non-editable field
		widgets = {
			'MEMO': forms.widgets.Textarea(attrs={'rows':10, 'cols': 30, 'style': 'resize:none;'}),
			'CONDITION': forms.widgets.Textarea(attrs={'rows':1, 'cols': 30, 'style': 'resize:none;'}),
		}




	 
