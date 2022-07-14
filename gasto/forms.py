from django import forms
from gasto.models import Gasto

class GastoForm ( forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ('categoria','importe','fecha','descripcion')
        widgets = {
            'fecha': forms.DateInput(format='%d%m%Y',attrs={'class':'form-control','type':'date'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'importe': forms.NumberInput(attrs={'class':'form-control',}),
            'categoria': forms.TextInput(attrs={'class':'form-control'}),
        }
        labels = {
            'fecha': ' ',
            'descripcion': ' ',
            'importe': ' ',
            'categoria': ' ',
        }