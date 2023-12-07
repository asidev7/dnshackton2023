from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django_countries.fields import CountryField


class CustomTextInput(forms.widgets.TextInput):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault('attrs', {}).update({'class': 'form-control'})
        super().__init__(*args, **kwargs)
    def __init__(self, *args, **kwargs):
        placeholder = kwargs.pop('placeholder', '')  # Retrieve the placeholder value (if provided)
        kwargs.setdefault('attrs', {}).update({'class': 'form-control', 'placeholder': placeholder})
        super().__init__(*args, **kwargs)

                
class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(widget=CustomTextInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(widget=CustomTextInput(), label='Nom d\'utilisateur')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Mot de passe')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}), label='Confirmer mot de passe')
    country = CountryField().formfield(widget=forms.Select(attrs={'class': 'form-control'},), label='Pays de residences')

    ROLE_CHOICES = [
        ('admin', 'Un admin'),
        ('client', 'Un client, '),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES,label=" Je suis ")
     # Set the default value for the "role" field
     
    role = forms.ChoiceField(
        choices=ROLE_CHOICES, 
        label="Je suis ",
        initial='Client'  # Set the initial value to 'patient'
    )
    class Meta:
        model = User
        fields = [ 'role', 'username', 'email','country', 'password1', 'password2',]

