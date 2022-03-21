from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre",required=True,max_length=60)
    email=forms.EmailField(label="Email",required=True, max_length=90)
    contenido=forms.CharField(label="contenido",required=False, max_length=300,widget=forms.Textarea(attrs={'rows': 5, 'cols': 100}))