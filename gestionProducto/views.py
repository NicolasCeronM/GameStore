from django.shortcuts import render
from . models import Producto

# Create your views here.

def juegos (request):

    juegos = Producto.objects.all()

    ctx={
        'juegos':juegos
    } 
    return render(request,'juegos.html', ctx)
