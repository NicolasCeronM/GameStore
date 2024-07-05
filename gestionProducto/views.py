from django.shortcuts import render
from . models import Producto
from django.db.models import Q

# Create your views here.

def juegos (request):

    juegos = Producto.objects.all()

    queryset = request.GET.get('buscador')

    if queryset:
        
        juegos = Producto.objects.filter(

            Q(nombre__icontains = queryset) 

        ).distinct()

        

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
