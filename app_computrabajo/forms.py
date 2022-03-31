from asyncio import current_task
from django import forms
from .models import Comentarios as contacto

class ComentariosForm(forms.ModelForm):

    class Meta:
        model = contacto
        fields = ["nombre", "correo_electronico", "telefono", "mensaje"]
        #fields = '__all__'

#nombre = forms.CharField(widget=forms.TextInput(attrs))