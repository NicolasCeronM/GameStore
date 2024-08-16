from django.contrib import admin
from .models import Plataforma, Producto , ImagenProducto

# Register your models here.

class ImagenProductoAdmin(admin.TabularInline):
    model = ImagenProducto

class PlataformaAdmin(admin.ModelAdmin):
    list_display =('nombre')

class ProductoAdmin(admin.ModelAdmin):
    inlines = [
        ImagenProductoAdmin
    ]

admin.site.register(Plataforma)
admin.site.register(Producto, ProductoAdmin)




