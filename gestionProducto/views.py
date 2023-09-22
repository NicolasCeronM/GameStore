from django.shortcuts import render
from . models import Producto

# Create your views here.

def juegos (request):

    juegos = Producto.objects.all()

    data={
        'juegos':juegos
    } 
    return render(request,'juegos.html', data)

def detalle_juego(request,producto_id):

    juego = Producto.objects.filter(id=producto_id)


    data ={
        'juego':juego
    }
    return render(request,'detalle_juego.html', data)
