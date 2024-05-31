from django.shortcuts import render,redirect
from .carro import Carro
from gestionProducto.models import Producto
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def vista_carro(request):

    return render(request,'carro.html')

@login_required
def agregar_producto(request,producto_id):

    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    #descuentos = Descuento.objects.all()

    # for descuento in descuentos:
    #     if producto == descuento.producto:
    #         producto.precio = round(producto.precio - (producto.precio * descuento.pct) / 100)
            
    carro.agregar(producto = producto)


    return redirect("dashboard:carro")

def eliminiar_producto(request,producto_id):

    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.eliminar(producto = producto)

    return redirect("index")

def restar_producto(request,producto_id):

    carro = Carro(request)

    producto = Producto.objects.get(id=producto_id)

    carro.restar_producto(producto = producto)

    return redirect("dashboard:carro")

def limpiar_carro(request):

    carro = Carro(request)
    carro.limpiar_carro()

    return redirect("dashboard:carro")