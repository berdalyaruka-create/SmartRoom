from django import forms
from .models import Rezerwacja

class RezerwacjaForm(forms.ModelForm):
    class Meta:
        model = Rezerwacja
        fields = ['data_start', 'data_koniec']
       
        labels = {
            'data_start': 'Początek rezerwacji',
            'data_koniec': 'Koniec rezerwacji',
        }
        widgets = {
            'data_start': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'data_koniec': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
        }