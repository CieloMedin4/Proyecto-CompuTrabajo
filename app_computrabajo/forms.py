from django import forms
from .models import Comentarios

class ComentariosForm(forms.ModelForm):

    class Meta:
        model = Comentarios
        fields = ["nombre", "correo_electronico", "telefono", "mensaje"]
        #fields = '__all__'

#nombre = forms.CharField(widget=forms.TextInput(attrs))