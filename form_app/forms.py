
from django import forms
from .models import FormData

class FormularioDados(forms.ModelForm):
    class Meta:
         
        model = FormData
        fields = ['nome', 'email', 'idade']