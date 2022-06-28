from django.contrib import admin
from .forms import ProductoForm
from app.models import *

class ProductoAdmin(admin.ModelAdmin):
    search_fields = ["nombre"]
    list_per_page = 5
    form = ProductoForm

admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(listaDeseado)
admin.site.register(Compra)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
