from asyncio import current_task
from django import forms
from .models import Comentarios as contacto
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class ComentariosForm(forms.ModelForm):

    class Meta:
        model = contacto
        fields = ["nombre", "correo_electronico", "telefono", "mensaje"]
        #fields = '__all__'

#nombre = forms.CharField(widget=forms.TextInput(attrs))

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'pasword2']


class loginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']
    username = forms.CharField(max_lenght=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-input'}) )
    password = forms.CharField(max_lenght=50, required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-input','data-toogle': 'password', 'id': 'password', 'name': 'password'}))
    remember_me = forms.BooleanField(required= False)
