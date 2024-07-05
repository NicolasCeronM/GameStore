from django.shortcuts import render, redirect
from . forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from gestionProducto.models import Producto
from django.db.models import Q
# Create your views here.


def home (request):

    #Seccion de buscador

    queryset = request.GET.get('buscador')
    print(queryset)

    if queryset:
        
        respuesta = Producto.objects.filter(
            Q(nombre__icontains = queryset)
        ).distinct()

    return render(request,'home.html')


def registro(request):

    form = CustomUserCreationForm

    data = {
        'form': form
    }

    if request.method=='POST':
        formulario = CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request,user)
            #Redirigir al home
            messages.success(request,'Registrado correctamente')
            return redirect(to='home')
        data["form"] = formulario


    return render(request,'registration/registro.html', data)
