# in your_app/forms.py
from django import forms
from main.models import Domaine



class DomaineDisponibiliteForm(forms.Form):
    nom_domaine = forms.CharField(
        label='Nom de domaine',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )