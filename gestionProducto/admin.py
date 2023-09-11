from django.contrib import admin
from .models import Plataforma, Producto

# Register your models here.

class PlataformaAdmin(admin.ModelAdmin):
    list_display =('nombre')

admin.site.register(Plataforma)
admin.site.register(Producto)

