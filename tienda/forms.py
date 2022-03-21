from django import forms
from django.forms import fields
from .models import Categoria,Producto

class CategoriaCreateForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ('nombre',)

class ProductoCreateForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre','categorias','imagen','precio','disponibilidad')