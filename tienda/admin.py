from django.contrib import admin
from .models import Categoria,Producto

# Register your models here.

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre','created']
    list_filter = ['created']
    readonly_fields = ('created','updated')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_filter = ['categorias','precio','disponibilidad']
    readonly_fields = ('created','updated')

#admin.site.register(Categoria,CategoriaAdmin)
#admin.site.register(Producto, ProductoAdmin)    